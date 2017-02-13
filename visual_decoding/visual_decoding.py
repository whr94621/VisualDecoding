from graphviz import Graph

__all__ = ['visual_decoding']

def _plot_sent(graph, sent, flag=None):
    prev = None
    if flag is not None:
        eos = 'EOS_%s' % flag
    else:
        eos = 'EOS'

    _sent = sent + [eos]
    for i, w in enumerate(_sent):
        n = '%s_%d' % (w, i)
        graph.node(n, w)
        if prev is not None:
            graph.edge(prev, n, label=flag)
        prev = n

    return graph

def visual_decoding(sent, saveto='tmp'):
    """
    Visualize multiple translation from machine translation.

    Example:
    >>> sentence = ['I have a apple',
                    'I have a dream',
                    'H have an egg']
    >>> visual_decoding(sent=sentence, saveto='demo')

    Args:
        sent: a list of str
            Multiple translations.

        saveto: str
            Graph will be saved as 'saveto.png'.

    Returns:
        None

    """
    graph = Graph(format='png',
                  node_attr={'shape':'box'},
                  graph_attr={'splines':'polyline'},
                  edge_attr={'dir':'forward'})

    graph.body.extend(['rankdir=LR'])

    for i,s in enumerate(sent):
        graph = _plot_sent(graph, s, flag=str(i))

    graph.render(filename=saveto, view=True)