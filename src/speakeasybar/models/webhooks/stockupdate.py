"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import drink_input as shared_drink_input
from ...models.shared import error as shared_error
from ...models.shared import ingredient_input as shared_ingredient_input
from dataclasses_json import Undefined, dataclass_json
from speakeasybar import utils
from typing import Optional


@dataclasses.dataclass
class StockUpdateResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    r"""An unknown error occurred interacting with the API."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class StockUpdateRequestBody:
    drink: Optional[shared_drink_input.DrinkInput] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('drink'), 'exclude': lambda f: f is None }})
    ingredient: Optional[shared_ingredient_input.IngredientInput] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ingredient'), 'exclude': lambda f: f is None }})
    

