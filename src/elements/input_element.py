from .base_element import BaseElement


class InputElement(BaseElement):
    @property
    def text(self):
        text = self.web_element.get_attribute("value")
        return text
