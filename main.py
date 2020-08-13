import _thread

from src.Models.tempcontrol import Tempcontrol

temppid = Tempcontrol(2 ,_thread.allocate_lock())

_thread.start_new_thread(temppid, ())
