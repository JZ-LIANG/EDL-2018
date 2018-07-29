
# Subline code for select region to show the mention
import sublime
import sublime_plugin

class SelectRegionCommand(sublime_plugin.WindowCommand):
    def highlight_region(self, regions):
        region_list = []
        if "," in regions:
            for region in regions.split(","):
                region_list.append(tuple(region.split("-")))
        else:
            region_list.append(tuple(regions.split("-")))

        view = self.window.active_view()
        view.show(int(region_list[0][0]))

        for region in region_list:
            begin = int(region[0])
            end = int(region[1])+1
            to_highlight = sublime.Region(begin, end)
            view.sel().add(to_highlight)

    def run(self):
        message = "Enter offset range(s) to select, separated by commas:"
        default = "0-100"
        self.window.show_input_panel(message, default, self.highlight_region, None, None)