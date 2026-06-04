from .theme import make_theme

# Aurora Borealis theme — created by GitHub Copilot
AURORA_THEME = make_theme(
    fontname='Arial',
    graph_bgcolor='#0d0d2b', graph_fontcolor='#f0f4ff',
    label_bgcolor='#1a0a3d',
    edge_color='#00f5d4',
    node_fillcolor='#0d2137', node_fontcolor='#c8f0ff',
    start_fillcolor='#00ff9f', start_fontcolor='#0d0d2b',
    end_fillcolor='#9b5de5', end_fontcolor='#f0f4ff',
    error_fillcolor='#ff4081', error_fontcolor='#0d0d2b', error_edge_color='#ff4081',
    warn_fillcolor='#fee440', warn_fontcolor='#0d0d2b', warn_edge_color='#fee440',
    info_fillcolor='#00bbf9', info_fontcolor='#0d0d2b', info_edge_color='#00bbf9',
    service_colors=[
        ('#00ff9f', '#0d0d2b'),  # Aurora green
        ('#00f5d4', '#0d0d2b'),  # Aurora cyan
        ('#00bbf9', '#0d0d2b'),  # Aurora blue
        ('#9b5de5', '#f0f4ff'),  # Aurora violet
        ('#f15bb5', '#0d0d2b'),  # Aurora pink
        ('#fee440', '#0d0d2b'),  # Aurora yellow
        ('#ff4081', '#0d0d2b'),  # Aurora rose
        ('#4cc9f0', '#0d0d2b'),  # Aurora sky
        ('#7b2fff', '#f0f4ff'),  # Deep violet
        ('#00c9a7', '#0d0d2b'),  # Deep teal
    ],
    group_colors=[
        ('#0d1a2e', '#00f5d4'),  # Night with cyan border
        ('#12062b', '#9b5de5'),  # Night with violet border
        ('#062b1a', '#00ff9f'),  # Night with green border
        ('#2b0620', '#f15bb5'),  # Night with pink border
        ('#1a1a06', '#fee440'),  # Night with yellow border
        ('#060e2b', '#00bbf9'),  # Night with blue border
        ('#1a062b', '#7b2fff'),  # Night with deep violet border
        ('#062b2b', '#00c9a7'),  # Night with teal border
    ],
)
