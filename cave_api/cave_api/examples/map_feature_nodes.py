def execute_command(session_data, socket, command="init", **kwargs):
    # Return the following app state (create a static app with no custom logic)
    return {
        "settings": {
            # Icon Url is used to load icons from a custom icon library
            # See the available versions provided by the cave team here:
            # https://react-icons.mitcave.com/versions.txt
            # Once you select a version, you can see the available icons in the version
            # EG: https://react-icons.mitcave.com/4.10.1/icon_list.txt
            "iconUrl": "https://react-icons.mitcave.com/4.10.1"
        },
        "appBar": {
            # Specify the order of items as they will appear in the app bar
            "order": {"data": ["refreshButton", "mapPage"]},
            "data": {
                # Add a simple button to the app bar to trigger the `init` command
                # This is useful for resetting the app to its initial state
                "refreshButton": {
                    "icon": "md/MdRefresh",
                    "apiCommand": "init",
                    "type": "button",
                    "bar": "upperLeft",
                },
                # Add an appBar button to launch a map focused dashboard
                "mapPage": {
                    "icon": "md/MdMap",
                    "type": "page",
                    "bar": "upperLeft",
                },
            },
        },
        "maps": {
            # Specify available map projections that can be selected in the dashboards by the user
            "data": {
                "exampleMap": {
                    "name": "Example Map",
                    # Specify the default projection for the map
                    # Note: globe can only be used if you have a mapbox token
                    "currentProjection": "globe",
                    # Specify the default viewport for the map
                    "defaultViewport": {
                        "longitude": -75.447,
                        "latitude": 40.345,
                        "zoom": 4.66,
                        "pitch": 0,
                        "bearing": 0,
                        "height": 1287,
                        "altitude": 1.5,
                        "maxZoom": 12,
                        "minZoom": 2,
                    },
                    "legendGroups": {
                        "facilities": {
                            "name": "Facilities",
                            "data": {
                                "warehouse": {
                                    "value": True,
                                    "sizeBy": "capacity",
                                    "colorBy": "includesAutomation",
                                    "colorByOptions": {
                                        "capacity": {
                                            "min": 0,
                                            "max": 100,
                                            "startGradientColor": "rgba(233, 0, 0, 255)",
                                            "endGradientColor": "rgba(96, 2, 2, 255)",
                                        },
                                        "includesAutomation": {
                                            "false": "rgba(255,0,0, 255)",
                                            "true": "rgba(0,255,0, 255)",
                                        },
                                    },
                                    "sizeByOptions": {
                                        "capacity": {"min": 0, "max": 80, "startSize": "30px", "endSize": "45px"},
                                    },
                                    "icon": "fa6/FaWarehouse",
                                },
                            },
                        },
                    },
                },
            },
        },
        "mapFeatures": {
            "data": {
                "warehouse": {
                    "type": "node",
                    "name": "Warehouse",
                    "props": {
                        "capacity": {
                            "name": "Capacity",
                            "type": "num",
                            "enabled": True,
                            "help": "The warehouse capacity in cubic feet",
                            "unit": "Cubic Feet",
                            "legendNotation": "precision",
                            "legendPrecision": 0,
                        },
                        "includesAutomation": {
                            "name": "Includes Automation",
                            "type": "toggle",
                            "enabled": True,
                            "help": "Whether the warehouse includes automation",
                        },
                    },
                    "data": {
                        "location": {
                            "latitude": [43.78, 39.82],
                            "longitude": [-79.63, -86.18],
                        },
                        "valueLists": {
                            "capacity": [100, 80],
                            "includesAutomation": [True, False],
                        },
                    }
                },
            }
        },
        # Add a map page to the app using the example map specified above
        "pages": {
            "currentPage": "mapPage",
            "data": {
                "mapPage": {
                    "pageLayout": [
                        {
                            "type": "map",
                            "mapId": "exampleMap",
                            "showToolbar": False,
                            "maximized": True},
                    ],
                },
            },
        },
    }
