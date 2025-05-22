# Add your plugins and plugin settings here.
# Of course uncomment this file out.

# To learn how to build images with your required plugins
# See https://github.com/netbox-community/netbox-docker/wiki/Using-Netbox-Plugins

PLUGINS = [
    "netbox_diode_plugin",
]

PLUGINS_CONFIG = {
    "netbox_diode_plugin": {
        # Diode gRPC target for communication with Diode server
        "diode_target_override": "grpc://localhost:8081/diode",

        # Username associated with changes applied via plugin
        "diode_username": "diode",

        # netbox-to-diode client_secret created during diode bootstrap.
        "netbox_to_diode_client_secret": "uYytVxfDmIb8iUeMreCOfThsx1h7ws8faAfkSthhWWM="
    },
}
