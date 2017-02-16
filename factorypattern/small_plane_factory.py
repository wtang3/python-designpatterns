from plane_factory_abs import PlaneFactoryAbs
from small_plane import SmallPlane

class SmallPlaneFactory(PlaneFactoryAbs):

    def create_plane(self):
        self.plane = SmallPlane()
        return self.plane