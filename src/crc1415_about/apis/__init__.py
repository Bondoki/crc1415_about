from nomad.config.models.plugins import APIEntryPoint


class MyAPIEntryPoint(APIEntryPoint):
    def load(self):
        from crc1415_about.apis.footer_pages import app

        return app


crc1415_about_footer_pages = MyAPIEntryPoint(
    prefix='crc1415_about',
    name='crc1415_about',
    description='CRC1415 Oasis footer pages.',
)
