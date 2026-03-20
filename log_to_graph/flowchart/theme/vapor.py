from .theme import make_theme

VAPORWAVE_THEME = make_theme(
    fontname='Monaco',
    graph_bgcolor='#2d0036', graph_fontcolor='#f8f8f2',
    label_bgcolor='#ff71ce',
    edge_color='#05ffa1',
    node_fillcolor='#01cdfe', node_fontcolor='#f8f8f2',
    start_fillcolor='#ff71ce', start_fontcolor='#2d0036',
    end_fillcolor='#05ffa1', end_fontcolor='#2d0036',
    error_fillcolor='#ff206e', error_fontcolor='#f8f8f2', error_edge_color='#ff206e',
    warn_fillcolor='#fbff12', warn_fontcolor='#2d0036', warn_edge_color='#fbff12',
    info_fillcolor='#01cdfe', info_fontcolor='#2d0036', info_edge_color='#01cdfe',
    service_colors=[
        ("#ff71ce", "#2d0036"),
        ("#01cdfe", "#2d0036"),
        ("#05ffa1", "#2d0036"),
        ("#fbff12", "#2d0036"),
        ("#b967ff", "#2d0036"),
        ("#ff206e", "#f8f8f2"),
        ("#f8f8f2", "#2d0036"),
        ("#2d0036", "#ff71ce"),
    ],
    group_colors=[
        ("#2d0036", "#ff71ce"),
        ("#2d0036", "#01cdfe"),
        ("#2d0036", "#05ffa1"),
        ("#2d0036", "#fbff12"),
        ("#2d0036", "#b967ff"),
        ("#2d0036", "#ff206e"),
        ("#2d0036", "#f8f8f2"),
        ("#ff71ce", "#2d0036"),
    ],
)
