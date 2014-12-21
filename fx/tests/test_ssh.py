from ..seq import Seq, perform_seq

from ..shell import Run, perform_run_locally
from ..ssh import Remote, perform_remote

from effect.dispatcher import TypeDispatcher
from effect import sync_perform, Effect


def test_stuff():
    dispatcher = TypeDispatcher({
        Run: perform_run_locally,
        Remote: perform_remote,
    })

    intent = Remote(
        host='localhost',
        effect=Effect(Run(command=['sh', '-c', 'echo -n $SSH_CONNECTION']))
    )
    result = sync_perform(dispatcher, Effect(intent))

    assert result.return_code == 0
    assert result.intent == intent.effect.intent
    assert result.output != ""


def test_seq():

    dispatcher = TypeDispatcher({
        Seq: perform_seq,
        Remote: perform_remote,
    })

    intent = Seq(effects=[
        Effect(Run(command=['echo', '-n', str(result)])) for result in range(5)])
    results = sync_perform(dispatcher, Effect(Remote(host="localhost", effect=Effect(intent))))

    assert [result.output for result in results] == map(str, range(5))
