import json
from bokeh.io import output_notebook, show, output_file
from bokeh.models import (CDSView, ColorBar, ColumnDataSource,
                          CustomJS, CustomJSFilter,
                          GeoJSONDataSource, HoverTool,
                          LinearColorMapper, Slider)
from bokeh.layouts import column, row, widgetbox
from bokeh.palettes import brewer
from bokeh.plotting import figure

def show_map(df, column, title, tip, order, low, high ):
    # Input GeoJSON source that contains features for plotting
    geosource = GeoJSONDataSource(geojson = df.to_json())

    # Define color palettes
    palette = brewer['Set1'][3]
    palette = palette[::order] # reverse order of colors so higher values have darker colors
    # Instantiate LinearColorMapper that linearly maps numbers in a range, into a sequence of colors.
    color_mapper = LinearColorMapper(palette = palette, low = low, high = high)
    # Define custom tick labels for color bar.
    tick_labels = {'0': '0', '4.0':'4.0', '6.5':'6.5','8':'>8'}
    # Create color bar.
    color_bar = ColorBar(color_mapper = color_mapper,
                         label_standoff = 5,
                         width = 500, height = 20,
                         border_line_color = None,
                         location = (0,0),
                         orientation = 'horizontal',
                         major_label_overrides = tick_labels)
    # Create figure object.
    p = figure(title = title,
               plot_height = 600, plot_width = 950,
               toolbar_location = 'below',
               tools = "pan, wheel_zoom, box_zoom, reset")
    p.xgrid.grid_line_color = None
    p.ygrid.grid_line_color = None
    # Add patch renderer to figure.
    countries = p.patches('xs','ys', source = geosource,
                       fill_color = {'field' :column,
                                     'transform' : color_mapper},
                       line_color = 'gray',
                       line_width = 0.25,
                       fill_alpha = 1)
    # Create hover tool
    p.add_tools(HoverTool(renderers = [countries],
                          tooltips = [('Country','@name'),
                                   (tip, '@'+column)]))
    # Specify layout
    p.add_layout(color_bar, 'below')

    #Display figure inline in Jupyter Notebook.
    output_notebook()

    #Display figure.
    show(p)