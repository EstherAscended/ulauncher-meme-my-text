from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction
import meme


class MemeExtension(Extension):

    def __init__(self):
        super(MemeExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        def append_to_list(list_to_append, name, description):
            list_to_append.append(ExtensionResultItem(icon='images/icon.png',
                                             name=name,
                                             description=description,
                                             on_enter=CopyToClipboardAction(description)))
        items = []
        for i in range(2):
            if i == 0:
                append_to_list(items, "Random Capitalization", meme.ran_cap(event.get_argument()))
            elif i == 1:
                append_to_list(items, "Vaporwave", meme.vaporwave(event.get_argument()))

        return RenderResultListAction(items)


if __name__ == '__main__':
    MemeExtension().run()
