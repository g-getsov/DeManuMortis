class TileMap:

    def __init__(self):
        self.tile_map = None
        self.tile_map_schema = None
        self.map_width = 0
        self.map_height = 0

    def construct_tile_map(self, tile_set, tile_map_schema_path):

        map_elements = ()
        map_schema = []
        tile_map = []

        tile_map_schema = open(tile_map_schema_path).read().split("$")

        for param in tile_map_schema:
            if "map_width=" in param:
                self.map_width = int(param.replace("map_width=", ""))
            elif "map_height=" in param:
                self.map_height = int(param.replace("map_height=", ""))
            elif "map=" in param:
                map_elements = param.replace("map=", "").split(",")

        map_elements.reverse()

        for idx_y in range(self.map_height):
            map_schema_row = []
            tile_map_row = []
            for idx_x in range(self.map_width):
                tile_index = int(map_elements.pop())
                map_schema_row.append(tile_index)
                tile_map_row.append(tile_set.get_tile(tile_index))

            map_schema.append(map_schema_row)
            tile_map.append(tile_map_row)

        self.tile_map_schema = map_schema
        self.tile_map = tile_map

    def draw(self, display_surface):
        for idx_y, tile_row in enumerate(self.tile_map):
            for idx_x, tile in enumerate(tile_row):
                display_surface.blit(tile.image, (idx_x*tile.width, idx_y*tile.height))
