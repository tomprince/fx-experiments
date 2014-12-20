from characteristic import attributes

from subprocess import Popen, PIPE

from effect import sync_performer

__all__ = ['Run', 'perform_run_locally']


@attributes([
    "command",
], apply_immutable=True)
class Run(object):
    """
    :ivar list command: Command to execute.
    """


@attributes([
    "intent",
    "return_code",
    "output",
], apply_immutable=True)
class ProcessResult(object):
    """
    :ivar Run process: Process that was run.
    :ivar int return_code: The return code of the program.
    :ivar bytes output: The output of the program.
    """


@sync_performer
def perform_run_locally(dispatcher, intent):
    process = Popen(args=intent.command, stdout=PIPE)
    output, _ = process.communicate()
    return_code = process.wait()
    return ProcessResult(
        intent=intent, return_code=return_code, output=output)
