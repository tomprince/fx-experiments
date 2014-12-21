from characteristic import attributes
from effect import perform, sync_performer
from effect.dispatcher import ComposedDispatcher, TypeDispatcher

from .shell import Run, ProcessResult


@attributes([
    'host',
    'effect',
], apply_immutable=True)
class Remote(object):
    pass


def perform_run_remotely(client):
    @sync_performer
    def performer(dispatcher, intent):
        from pipes import quote as shell_quote
        command = ' '.join(map(shell_quote, intent.command))
        stdin, stdout, stderr = client.exec_command(command)
        return ProcessResult(
            intent=intent, return_code=stdout.channel.recv_exit_status(),
            output=stdout.read())

    return performer


def perform_remote(dispatcher, intent, box):
    from paramiko import SSHClient
    client = SSHClient()
    client.load_system_host_keys()
    client.connect(intent.host)

    remote_runner = perform_run_remotely(client=client)
    dispatcher = ComposedDispatcher(dispatchers=[
        TypeDispatcher({Run: remote_runner}),
        dispatcher
    ])

    # TODO: fail
    def close(_):
        client.close()
        return _
    perform(dispatcher, intent.effect.on(success=close)
            .on(success=box.succeed, error=box.fail))
