"""Constants for the Cardiff Waste integration."""

DOMAIN = "cardiffwaste"

ATTR_COLLECTION_TYPE = "collection_type"
ATTR_IMAGE_URL = "image_URL"

CONF_UPRN = "uprn"

TYPE_FOOD = "food"
TYPE_GARDEN = "garden"
TYPE_GENERAL = "general"
TYPE_HYGIENE = "hygiene"
TYPE_RECYCLING = "recycling"

ALL_COLLECTIONS = [TYPE_GARDEN, TYPE_GENERAL, TYPE_FOOD, TYPE_HYGIENE, TYPE_RECYCLING]

DEFAULT_OPTIONS = {
    TYPE_FOOD: True,
    TYPE_GARDEN: True,
    TYPE_GENERAL: True,
    TYPE_HYGIENE: False,
    TYPE_RECYCLING: True,
}
