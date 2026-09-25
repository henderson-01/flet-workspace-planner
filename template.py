"""
Workspace Planner, Flet Desktop/Web GUI Template

This script builds a modern dark-themed dashboard using the Flet Python library.
It features a persistent sidebar navigation and a two-column main workspace
containing an interactive task manager, Daily Planner and a multi-line notebook.
"""

import flet as ft


def main(page: ft.Page):
    """
    Main application entry point where the Flet UI components and layout are assembled.

    Args:
        page ft.Page: The top-level canvas/window instance provided by Flet.
    """

    # GLOBAL PAGE CONFIGURATION.

    page.title = "Workspace Planner"
    page.padding = 0  # Remove window borders/padding for edge-to-edge layout
    page.theme_mode = ft.ThemeMode.DARK  # Enforce dark theme
    page.bgcolor = "#09090B"  # Deep dark background color Zinc/Slate dark tone


    # EVENT HANDLERS & CALLBACKS.

    def hover_lift(e):
        """
        Event handler triggered when hovering over interactive cards.
        Slightly increases card scale to create a subtle 3D lift visual effect.
        """
        e.control.scale = 1.01 if e.data == "true" else 1.00
        e.control.update()

    def add_task(_):
        """
        Event handler triggered to create a new task.
        Reads text input, appends a Checkbox widget to the task list, clears the input,
        and refreshes the UI page state.
        """
        if new_task_input.value:
            task_list.controls.append(
                ft.Checkbox(label=new_task_input.value, fill_color="#10B981")
            )
            new_task_input.value = ""  # Clear text field after submission
            page.update()  # Refresh the UI to show the new item


    # NAVIGATION SIDEBAR COMPONENTS.

    nav_items = [
        # User profile / Workspace avatar header
        ft.Row(
            controls=[
                ft.CircleAvatar(
                    radius=18, foreground_image_src="https://picsum.photos/200"
                ),
                ft.Text(
                    value="My Workspace",
                    size=15,
                    weight=ft.FontWeight.W_600,
                    color="white",
                ),
            ]
        ),
        ft.Divider(height=40, color="white10"),  # Horizontal subtle separator
        # Primary navigation action buttons
        ft.TextButton(
            content="Daily Planner",
            icon=ft.Icons.CALENDAR_TODAY,
            icon_color="white54",
            style=ft.ButtonStyle(color="white"),
        ),
        ft.TextButton(
            content="Notebook",
            icon=ft.Icons.EDIT_NOTE,
            icon_color="white54",
            style=ft.ButtonStyle(color="white70"),
        ),
        ft.TextButton(
            content="Focus Timer",
            icon=ft.Icons.TIMER,
            icon_color="white54",
            style=ft.ButtonStyle(color="white70"),
        ),
        ft.Container(expand=True),  # Flexible spacer to push Settings to bottom
        ft.TextButton(
            content="Settings",
            icon=ft.Icons.SETTINGS,
            icon_color="white54",
            style=ft.ButtonStyle(color="white70"),
        ),
    ]

    # Sidebar container wrapping the navigation elements
    sidebar = ft.Container(
        width=250,  # Fixed width for the sidebar panel
        bgcolor="#09090B",
        border=ft.Border.only(right=ft.BorderSide(1, "white10")),  # Right border divider
        padding=25,
        content=ft.Column(controls=nav_items),
    )


    # DAILY PLANNER WIDGETS.

    # Input field for typing new tasks
    new_task_input = ft.TextField(
        hint_text="What needs to be done?",
        expand=True,  # Fills available horizontal width in its row
        border_color="white10",
        focused_border_color="#10B981",  # Accent emerald border on active focus
        content_padding=15,
        border_radius=8,
        text_size=14,
    )

    # Dynamic vertical container storing the list of task Checkboxes
    task_list = ft.Column(
        controls=[
            ft.Checkbox(
                label="Review weekly analytics report", value=True, fill_color="#10B981"
            ),
            ft.Checkbox(label="Draft project proposal", fill_color="#10B981"),
            ft.Checkbox(label="Sync with design team", fill_color="#10B981"),
        ]
    )

    # Main Planner Card component wrapper
    planner_card = ft.Container(
        expand=1,  # Shared equal horizontal space with notebook card
        bgcolor="#121214",
        border_radius=12,
        border=ft.Border.all(1, "white10"),
        padding=30,
        animate_scale=ft.Animation(300, ft.AnimationCurve.EASE_OUT),  # Smooth scaling transition
        on_hover=hover_lift,  # Apply hover micro-interaction
        content=ft.Column(
            controls=[
                # Card Header
                ft.Row(
                    controls=[
                        ft.Icon(icon=ft.Icons.TASK_ALT, color="#10B981", size=24),
                        ft.Text(
                            value="Today's Agenda",
                            size=18,
                            weight=ft.FontWeight.BOLD,
                            color="white",
                        ),
                    ]
                ),
                ft.Divider(height=20, color="transparent"),
                # Input controls row TextField + Submit Button
                ft.Row(
                    controls=[
                        new_task_input,
                        ft.IconButton(
                            icon=ft.Icons.ADD_BOX,
                            icon_color="#10B981",
                            icon_size=35,
                            on_click=add_task,  # Attaches task addition handler
                        ),
                    ]
                ),
                ft.Divider(height=20, color="transparent"),
                # Render the active task list
                task_list,
            ]
        ),
    )


    # NOTEBOOK WIDGETS.

    # Main Quick Notes Card component wrapper
    notebook_card = ft.Container(
        expand=1,  # Shared equal horizontal space with planner card
        bgcolor="#121214",
        border_radius=12,
        border=ft.Border.all(1, "white10"),
        padding=30,
        animate_scale=ft.Animation(300, ft.AnimationCurve.EASE_OUT),  # Smooth scaling transition
        on_hover=hover_lift,  # Apply hover micro-interaction
        content=ft.Column(
            controls=[
                # Card Header
                ft.Row(
                    controls=[
                        ft.Icon(icon=ft.Icons.BOOKMARK, color="#A1A1AA", size=24),
                        ft.Text(
                            value="Quick Notes",
                            size=18,
                            weight=ft.FontWeight.BOLD,
                            color="white",
                        ),
                    ]
                ),
                ft.Divider(height=20, color="transparent"),
                # Multiline text input simulating a notepad line area
                ft.TextField(
                    multiline=True,
                    min_lines=8,
                    max_lines=8,
                    hint_text="Jot down some thoughts...",
                    border=ft.InputBorder.NONE,  # Borderless appearance for clean notepad feel
                    text_size=14,
                ),
            ]
        ),
    )


    # MAIN WORKSPACE AREA & ROOT LAYOUT.

    # Right-side main content wrapper holding headers and workspace cards
    main_content = ft.Container(
        expand=True,  # Expands to consume remaining canvas width
        padding=40,
        content=ft.Column(
            controls=[
                # Page Greeting Header
                ft.Text(
                    value="Good Morning.",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color="white",
                ),
                ft.Text(value="Let's make today productive.", size=16, color="white54"),
                ft.Divider(height=30, color="transparent"),
                # Side-by-side card section Planner + Notebook
                ft.Row(expand=True, spacing=30, controls=[planner_card, notebook_card]),
            ]
        ),
    )

    # Mount the top-level row Sidebar + Main Content to the active window page
    page.add(ft.Row(expand=True, spacing=0, controls=[sidebar, main_content]))


# APPLICATION ENTRY POINT.

if __name__ == "__main__":
    ft.run(main)  # Launches the Flet GUI application window
