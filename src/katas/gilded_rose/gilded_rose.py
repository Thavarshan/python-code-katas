from ..exceptions.illegal_argument_error import IllegalArgumentError
import importlib


class GildedRose:

    items = {
        'normal': 'Normal',
        'Aged Brie': 'Brie',
        'Sulfuras, Hand of Ragnaros': 'Sulfuras',
        'Backstage passes to a TAFKAL80ETC concert': 'BackstagePasses',
        'Conjured Juna Cake': 'Conjured',
    }

    def of(self, name, quality, sell_in):
        if name in self.items:
            module = importlib.import_module(
                'src.katas.gilded_rose.item_factory')
            class_ = getattr(module, self.items[name])

            return class_(quality, sell_in)

        raise IllegalArgumentError('Item type does not exist.')
