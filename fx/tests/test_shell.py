from ..shell import Run, perform_run_locally

from effect.dispatcher import TypeDispatcher
from effect import sync_perform, Effect


def test_stuff():

    dispatcher = TypeDispatcher({Run: perform_run_locally})

    intent = Run(command=['echo', 'hi'])
    result = sync_perform(dispatcher, Effect(intent))

    assert result.return_code == 0
    assert result.intent == intent
    assert result.output == "hi\n"
