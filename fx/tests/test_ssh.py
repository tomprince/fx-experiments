
from ..shell import Run, perform_run_locally
from ..ssh import Remote, perform_remote

from effect.dispatcher import TypeDispatcher
from effect import sync_perform, Effect


def test_stuff(monkeypatch):

    import sys
    monkeypatch.setattr(sys, 'stdin', open('/dev/null'))
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
