from enum import Enum
from pydantic import BaseModel, validator, ValidationError, parse_obj_as
from typing import List, Optional, Union


class MetricType(str, Enum):
    ALL_SIZE_SINGLE_COLOR = "all_size_-_single_color"
    SINGLE_SIZE_ALL_COLOR = "single_size_-_all_colors"
    DIFFERENT_SIZE_DIFFERENT_COLOR = "different_size_-_different_color"

    @property
    def alias(self):
        return self.value.replace("_", " ")

    @classmethod
    def list(cls):
        return list(map(lambda c: c.alias, cls))


class DefinitionType(str, Enum):
    EACHES = "eaches"
    PACKS = "packs"
    CARTONS = "cartons"
    BOXS = 'boxes'


class UnitMappingMetricsValues(BaseModel):
    size: Optional[str] = None
    color: Optional[str] = None
    value: int
    product_code: Union[int, str]


class UnitMappingMetrics(BaseModel):
    size_list: Optional[List[str]]
    colour_list: Optional[List[str]]
    values: List[UnitMappingMetricsValues]


class UnitDefinition(BaseModel):
    definition_type: DefinitionType
    name: str
    description: str
    pack_quantity: int
    cartons_in_box_quantity: Optional[int] = None
    packs_in_carton_quantity: Optional[int] = None
    metric_type: str
    metrics: UnitMappingMetrics


class UnitDefinitionPostBody(BaseModel):
    definition_type: DefinitionType
    name: str
    description: str
    pack_quantity: int
    cartons_in_box_quantity: Optional[int] = None
    packs_in_carton_quantity: Optional[int] = None
    metric_type: str
    metrics: List[UnitMappingMetricsValues]

    @validator('metric_type')
    def validate_metric_type(cls, v, values, **kwargs):
        if v not in MetricType.list():
            raise ValueError(f'Metric type must be one of {MetricType.list()}')
        return v


if __name__ == '__main__':
    try:
        metrics = [{
                    "size": "3XL",
                    "color": "PUMA BLACK",
                    "value": 0,
                    "product_code": "889183844102"
                },
                {
                    "size": "M",
                    "color": "MEDIUM GRAY HEATHER",
                    "value": 16,
                    "product_code": "889183844232"
                },
                {
                    "size": "M",
                    "color": "PUMA BLACK",
                    "value": 0,
                    "product_code": "889183844676"
                },
                {
                    "size": "S",
                    "color": "MEDIUM GRAY HEATHER",
                    "value": 16,
                    "product_code": "889183844096"
                },
                {
                    "size": "XXL",
                    "color": "MEDIUM GRAY HEATHER",
                    "value": 16,
                    "product_code": "889183844287"
                },
                {
                    "size": "L",
                    "color": "MEDIUM GRAY HEATHER",
                    "value": 16,
                    "product_code": "889183844157"
                },
                {
                    "size": "XXL",
                    "color": "PUMA BLACK",
                    "value": 0,
                    "product_code": "889183844713"
                },
                {
                    "size": "L",
                    "color": "PUMA BLACK",
                    "value": 0,
                    "product_code": "889183844850"
                },
        ]

        metrics = parse_obj_as(List[UnitMappingMetricsValues], metrics)

        data = {
            "name": "First",
            "description": "First",
            "definition_type": "pack",
            "metric_type": "all size - single colo",
            "pack_quantity": 96,
            "packs_in_carton_quantity": 0,
            "cartons_in_box_quantity": 0,
            "metrics": metrics
        }

        child = UnitDefinitionPostBody(**data)
    except ValidationError as e:
        print(e.json())
    else:
        print('No ValidationError caught.')
        # > No ValidationError caught.