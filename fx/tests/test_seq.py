from ..seq import Seq, perform_seq

from effect.dispatcher import TypeDispatcher, ComposedDispatcher
from effect import sync_perform, Effect, base_dispatcher, ConstantIntent


def test_stuff():

    dispatcher = ComposedDispatcher(dispatchers=[
        TypeDispatcher({Seq: perform_seq}),
        base_dispatcher,
    ])

    intent = Seq(effects=[
        Effect(ConstantIntent(result=result)) for result in range(5)])
    result = sync_perform(dispatcher, Effect(intent))

    assert result == list(range(5))
