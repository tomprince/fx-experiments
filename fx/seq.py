from characteristic import attributes
from effect import perform


@attributes([
    'effects',
], apply_immutable=True)
class Seq(object):
    pass


def perform_seq(dispatcher, intent, box):
    results = []
    effects = [effect.on(success=results.append) for effect in intent.effects]
    composite = effects[0]
    # TODO: failures
    for effect in effects[1:]:
        composite = composite.on(success=lambda _, effect=effect: effect)
    perform(dispatcher, composite.on(success=lambda _: box.succeed(results)))
