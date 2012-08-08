import matplotlib.pyplot as plt

### Constatns
COLORS = ['r','b', 'g','c','m']
LOAD_AVERAGE = {
    'ylabel': 'load average',
    'items': ['r', 'b']}
CPU = {
    'ylabel': 'cpu [%]',
    'items': ['us', 'sy', 'id', 'wa']}
MEMORY = {
    'ylabel': 'memory [MiB]',
    'items': ['swpd', 'free', 'buff', 'cache']}
BIO = {
    'ylabel': 'block io [blocks/s]',
    'items': ['bi', 'bo']}

### Implementation
class VmstatPlot(object):
    def __init__(self, data, graphs, interval, title):
        self._data = data
        self._graphs = graphs
        self._title = title if title is not None else 'vmstat'
        self._interval = interval

    def _plot_graph(self, time, graph):
        items = graph['items']
        plot_cmd = []
        for i, item in enumerate(items):
            plot_cmd.extend([time, self._data.__getattr__(item), '%s-' % COLORS[i]])
        plt.plot(*plot_cmd)
        plt.legend(items, loc=0)
        plt.ylabel(graph['ylabel'])
        item_max = max([self._data.__getattr__('%s_max' % item) for item in items])
        plt.axis(ymin=item_max * -0.1, ymax=item_max * 1.1)

    def plot(self, filename):
        plt.figure(num=None, figsize=(8, len(self._graphs) * 4), facecolor='w', edgecolor='k')
        length = len(self._data.__getattr__(self._graphs[0]['items'][0]))
        t = range(0, length * self._interval, self._interval)
        for i, graph in enumerate(self._graphs):
            plt.subplot(len(self._graphs),1,i+1)
            self._plot_graph(t, graph)
            if i == 0:
                plt.title(self._title)
            if i == len(self._graphs) - 1:
                plt.xlabel('time [s]')
        plt.savefig(filename)
