import itertools
import inspect
import conso
from conso import widgets



class BookmarksModule(widgets.ListModule):
    pass

#r = widgets.VLayout(
#    widgets.VListBox(widgets.SimpleListModel(["foo%d" % (i,) for i in range(100)])),
#    widgets.HListBox(widgets.SimpleListModel(["bar%d" % (i,) for i in range(20)])),
#)


if __name__ == "__main__":
    r = BookmarksModule([widgets.TextEntry("hello %d" % (i,)) for i in range(50)])
    app = conso.Application(r)
    app.run(exit = False)












