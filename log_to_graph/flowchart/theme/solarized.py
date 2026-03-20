from .theme import make_theme

SOLARIZED_THEME = make_theme(
    fontname='Fira Mono',
    graph_bgcolor='#fdf6e3', graph_fontcolor='#657b83',
    label_bgcolor='#eee8d5',
    edge_color='#b58900',
    node_fillcolor='#b58900', node_fontcolor='#fdf6e3',
    start_fillcolor='#2aa198', start_fontcolor='#fdf6e3',
    end_fillcolor='#268bd2', end_fontcolor='#fdf6e3',
    error_fillcolor='#dc322f', error_fontcolor='#fdf6e3', error_edge_color='#dc322f',
    warn_fillcolor='#b58900', warn_fontcolor='#fdf6e3', warn_edge_color='#b58900',
    info_fillcolor='#2aa198', info_fontcolor='#fdf6e3', info_edge_color='#2aa198',
    service_colors=[
        ("#b58900", "#fdf6e3"),
        ("#2aa198", "#fdf6e3"),
        ("#268bd2", "#fdf6e3"),
        ("#dc322f", "#fdf6e3"),
        ("#859900", "#fdf6e3"),
        ("#6c71c4", "#fdf6e3"),
    ],
    group_colors=[
        ("#eee8d5", "#657b83"),
        ("#fdf6e3", "#657b83"),
        ("#b58900", "#fdf6e3"),
        ("#2aa198", "#fdf6e3"),
    ],
)
