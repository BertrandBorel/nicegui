from nicegui import ui, app, events
from nicegui.elements.mixins.disableable_element import DisableableElement
from nicegui.elements.mixins.value_element import ValueElement
from typing import Optional, Callable, Any, Tuple


class Range(DisableableElement):

    def __init__(
            self, min: int, max: int, *, value: Tuple[int, int] = None, vertical: bool = False, snap: bool = False,
            label_always: bool = False, on_change: Optional[Callable[..., Any]] = None) -> None:
        super().__init__(tag='q-range')
        self._props['min'] = min
        self._props['max'] = max
        self._props['snap'] = snap
        self._props['vertical'] = vertical
        self._props['label-always'] = label_always
        self.on_change = on_change

        if value is None:
            self._props['model-value'] = {'min':min, 'max':max}
        else:
            self._props['model-value'] = {'min':value[0], 'max':value[1]}

        if on_change:
            self.on("update:model-value", self.handle_change)

    def handle_change(self, e: events.GenericEventArguments):
        self._props["model-value"] = e.args
        self.update()
        self.on_change((e.args["min"], e.args["max"]) )

       


a = Range(1, 10, value=(3,4))



ui.run()
