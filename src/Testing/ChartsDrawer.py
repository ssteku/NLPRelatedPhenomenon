import pygal
from pygal.style import BlueStyle, LightSolarizedStyle
import datetime
from pygal.style import Style

class ChartsDrawer(object):
    def __init__(self):
        pass
        self.__fill = False
        self.__legend_at_bottom = True

    def create_charts(self, testcase, value_range):
        results = testcase['results']
        line_chart = self.__create_line_chart(testcase)

        chart_title = "Results/" + self.__get_datetime_string() + testcase['title']
        classifier_charts = self.__create_classifiers_charts_maps(results['levels']['1'].keys(), testcase)
        for level in  results['levels'].keys():
            level_line_chart = self.__create_line_chart(testcase)
            for value_class in results['levels'][level].keys():
                self.__set_chart_properties(line_chart, value_range, testcase)
                self.__set_chart_properties(level_line_chart, value_range, testcase)
                self.__set_chart_properties(classifier_charts[value_class], value_range, testcase)
                series_string = "Processing level: " + level + ', classifier: ' + value_class
                print "Processing level: " + level + ' , classifier: ' + value_class

                classifier_charts[value_class].add(series_string, results['levels'][level][value_class])

                line_chart.add(series_string, results['levels'][level][value_class])
                level_line_chart.add(series_string, results['levels'][level][value_class])

            self.__render_chart(level_line_chart, chart_title + "_level_" + level)
        self.__render_chart(line_chart, chart_title)
        for classifier in classifier_charts:
            self.__render_chart(classifier_charts[classifier], chart_title + "_classifier_" + classifier)

    def __set_chart_properties(self, chart, value_range, testcase):
        chart.title = testcase['description']
        chart.x_labels = map(str, value_range)

    def __ctreate_style(self):
        return Style(opacity_hover='.4', opacity='.8', background='white',
                plot_background='rgba(0, 0, 255, 0.05)',
                foreground='rgba(0, 0, 0, 0.8)',
                foreground_light='rgba(0, 0, 0, 0.9)',
                foreground_dark='rgba(0, 0, 0, 0.7)',
                colors=('#5DA5DA', '#FAA43A',
                            '#60BD68', '#F17CB0', '#4D4D4D', '#B2912F',
                            '#B276B2', '#DECF3F', '#F15854'))

    def __get_datetime_string(self):
        return datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S_")

    def __create_classifiers_charts_maps(self, classifiers, testcase):
        charts_map = {}
        for classifier in classifiers:
            charts_map[classifier] = self.__create_line_chart(testcase)
        return charts_map

    def __create_line_chart(self, testcase):
        return pygal.Line(
            width=1600, height=960,
            title_font_size=24, fill=self.__fill,
            truncate_legend=65, style=self.__ctreate_style(),
            x_label_rotation=45, legend_at_bottom=self.__legend_at_bottom,
            print_values=False,
            x_title=testcase['x_title'], y_title=testcase['y_title'],
            legend_font_size=18, dots_size=5,
            label_font_size=16)

    def __render_chart(self, chart, title):
        print "Rendering chart: " + title
        chart.render_to_png(title + '.png')
        chart.render_to_file(title)