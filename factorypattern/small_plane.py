from plane_abs import PlaneAbs

class SmallPlane(PlaneAbs):

    def start_engine(self):
        return "Small Plane is flying"

    def stop_engine(self):
        return "Small Plane has stopped"