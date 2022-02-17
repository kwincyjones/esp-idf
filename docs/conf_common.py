# -*- coding: utf-8 -*-
#
# Common (non-language-specific) configuration for Sphinx
#
# This file is imported from a language-specific conf.py (ie en/conf.py or
# zh_CN/conf.py)

# type: ignore
# pylint: disable=wildcard-import
# pylint: disable=undefined-variable

from __future__ import print_function, unicode_literals

import os.path
import re

from esp_docs.conf_docs import *  # noqa: F403,F401

if os.environ.get('IDF_PATH') is None:
    raise RuntimeError('IDF_PATH should be set, run export.sh before building docs')

BT_DOCS = ['api-guides/blufi.rst',
           'api-guides/esp-ble-mesh/**',
           'api-reference/bluetooth/bt_le.rst',
           'api-reference/bluetooth/esp_bt_defs.rst',
           'api-reference/bluetooth/esp_bt_device.rst',
           'api-reference/bluetooth/esp_bt_main.rst',
           'api-reference/bluetooth/bt_common.rst',
           'api-reference/bluetooth/controller_vhci.rst',
           'api-reference/bluetooth/esp_gap_ble.rst',
           'api-reference/bluetooth/esp_gatt_defs.rst',
           'api-reference/bluetooth/esp_gatts.rst',
           'api-reference/bluetooth/esp_gattc.rst',
           'api-reference/bluetooth/esp_blufi.rst',
           'api-reference/bluetooth/esp-ble-mesh.rst',
           'api-reference/bluetooth/index.rst',
           'api-reference/bluetooth/nimble/index.rst']

CLASSIC_BT_DOCS = ['api-reference/bluetooth/classic_bt.rst',
                   'api-reference/bluetooth/esp_a2dp.rst',
                   'api-reference/bluetooth/esp_avrc.rst',
                   'api-reference/bluetooth/esp_hf_defs.rst',
                   'api-reference/bluetooth/esp_hf_client.rst',
                   'api-reference/bluetooth/esp_hf_ag.rst',
                   'api-reference/bluetooth/esp_spp.rst',
                   'api-reference/bluetooth/esp_gap_bt.rst']

WIFI_DOCS = ['api-guides/wifi.rst',
             'api-guides/wifi-security.rst',
             'api-guides/wireshark-user-guide.rst']

SDMMC_DOCS = ['api-reference/peripherals/sdmmc_host.rst',
              'api-reference/peripherals/sd_pullup_requirements.rst']

SDIO_SLAVE_DOCS = ['api-reference/peripherals/sdio_slave.rst',
                   'api-reference/protocols/esp_sdio_slave_protocol.rst']

MCPWM_DOCS = ['api-reference/peripherals/mcpwm.rst']

DEDIC_GPIO_DOCS = ['api-reference/peripherals/dedic_gpio.rst']

PCNT_DOCS = ['api-reference/peripherals/pcnt.rst']

RMT_DOCS = ['api-reference/peripherals/rmt.rst']

DAC_DOCS = ['api-reference/peripherals/dac.rst']

TEMP_SENSOR_DOCS = ['api-reference/peripherals/temp_sensor.rst']

TOUCH_SENSOR_DOCS = ['api-reference/peripherals/touch_pad.rst']

SPIRAM_DOCS = ['api-guides/external-ram.rst']

USB_DOCS = ['api-reference/peripherals/usb_device.rst',
            'api-reference/peripherals/usb_host.rst',
            'api-guides/usb-otg-console.rst',
            'api-guides/dfu.rst']

FTDI_JTAG_DOCS = ['api-guides/jtag-debugging/configure-ft2232h-jtag.rst']

USB_SERIAL_JTAG_DOCS = ['api-guides/jtag-debugging/configure-builtin-jtag.rst',
                        'api-guides/usb-serial-jtag-console.rst']

ULP_DOCS = ['api-guides/ulp.rst', 'api-guides/ulp_macros.rst']

RISCV_COPROC_DOCS = ['api-guides/ulp-risc-v.rst',]

XTENSA_DOCS = ['api-guides/hlinterrupts.rst',
               'api-reference/system/perfmon.rst']

RISCV_DOCS = []  # type: list[str]

TWAI_DOCS = ['api-reference/peripherals/twai.rst']

SIGMADELTA_DOCS = ['api-reference/peripherals/sigmadelta.rst']

I2S_DOCS = ['api-reference/peripherals/i2s.rst']

ESP32_DOCS = ['api-guides/ulp_instruction_set.rst',
              'api-reference/system/himem.rst',
              'api-guides/romconsole.rst',
              'api-reference/system/ipc.rst',
              'security/secure-boot-v1.rst',
              'api-reference/peripherals/secure_element.rst',
              'api-reference/peripherals/dac.rst',
              'hw-reference/esp32/**',
              'api-guides/RF_calibration.rst'] + FTDI_JTAG_DOCS

ESP32S2_DOCS = ['hw-reference/esp32s2/**',
                'api-guides/ulp_extended_instruction_set.rst',
                'api-guides/usb-console.rst',
                'api-reference/peripherals/ds.rst',
                'api-reference/peripherals/spi_slave_hd.rst',
                'api-reference/peripherals/temp_sensor.rst',
                'api-reference/system/async_memcpy.rst',
                'api-reference/peripherals/touch_element.rst',
                'api-guides/RF_calibration.rst'] + FTDI_JTAG_DOCS

ESP32S3_DOCS = ['hw-reference/esp32s3/**',
                'api-guides/ulp_extended_instruction_set.rst',
                'api-reference/system/ipc.rst',
                'api-guides/flash_psram_config.rst',
                'api-guides/RF_calibration.rst']

# No JTAG docs for this one as it gets gated on SOC_USB_SERIAL_JTAG_SUPPORTED down below.
ESP32C3_DOCS = ['hw-reference/esp32c3/**',
                'api-guides/RF_calibration.rst']

# format: {tag needed to include: documents to included}, tags are parsed from sdkconfig and peripheral_caps.h headers
conditional_include_dict = {'SOC_BT_SUPPORTED':BT_DOCS,
                            'SOC_WIFI_SUPPORTED':WIFI_DOCS,
                            'SOC_CLASSIC_BT_SUPPORTED':CLASSIC_BT_DOCS,
                            'SOC_SDMMC_HOST_SUPPORTED':SDMMC_DOCS,
                            'SOC_SDIO_SLAVE_SUPPORTED':SDIO_SLAVE_DOCS,
                            'SOC_MCPWM_SUPPORTED':MCPWM_DOCS,
                            'SOC_USB_OTG_SUPPORTED':USB_DOCS,
                            'SOC_USB_SERIAL_JTAG_SUPPORTED':USB_SERIAL_JTAG_DOCS,
                            'SOC_DEDICATED_GPIO_SUPPORTED':DEDIC_GPIO_DOCS,
                            'SOC_SPIRAM_SUPPORTED':SPIRAM_DOCS,
                            'SOC_PCNT_SUPPORTED':PCNT_DOCS,
                            'SOC_RMT_SUPPORTED':RMT_DOCS,
                            'SOC_DAC_SUPPORTED':DAC_DOCS,
                            'SOC_TOUCH_SENSOR_NUM':TOUCH_SENSOR_DOCS,
                            'SOC_ULP_SUPPORTED':ULP_DOCS,
                            'SOC_RISCV_COPROC_SUPPORTED':RISCV_COPROC_DOCS,
                            'SOC_DIG_SIGN_SUPPORTED':['api-reference/peripherals/ds.rst'],
                            'SOC_HMAC_SUPPORTED':['api-reference/peripherals/hmac.rst'],
                            'SOC_ASYNC_MEMCPY_SUPPORTED':['api-reference/system/async_memcpy.rst'],
                            'CONFIG_IDF_TARGET_ARCH_XTENSA':XTENSA_DOCS,
                            'CONFIG_IDF_TARGET_ARCH_RISCV':RISCV_DOCS,
                            'SOC_TEMP_SENSOR_SUPPORTED':TEMP_SENSOR_DOCS,
                            'SOC_TWAI_SUPPORTED':TWAI_DOCS,
                            'SOC_I2S_SUPPORTED':I2S_DOCS,
                            'SOC_SIGMADELTA_SUPPORTED':SIGMADELTA_DOCS,
                            'esp32':ESP32_DOCS,
                            'esp32s2':ESP32S2_DOCS,
                            'esp32s3':ESP32S3_DOCS,
                            'esp32c3':ESP32C3_DOCS}

extensions += ['sphinx_copybutton',
               # Note: order is important here, events must
               # be registered by one extension before they can be
               # connected to another extension
               'esp_docs.idf_extensions.build_system',
               'esp_docs.idf_extensions.esp_err_definitions',
               'esp_docs.idf_extensions.gen_toolchain_links',
               'esp_docs.idf_extensions.gen_defines',
               'esp_docs.idf_extensions.gen_version_specific_includes',
               'esp_docs.idf_extensions.kconfig_reference',
               'esp_docs.idf_extensions.gen_idf_tools_links',
               'esp_docs.esp_extensions.run_doxygen',
               ]

# link roles config
github_repo = 'espressif/esp-idf'

# context used by sphinx_idf_theme
html_context['github_user'] = 'espressif'
html_context['github_repo'] = 'esp-idf'

# Extra options required by sphinx_idf_theme
project_slug = 'esp-idf'
versions_url = 'https://dl.espressif.com/dl/esp-idf/idf_versions.js'

idf_targets = ['esp32', 'esp32s2', 'esp32s3', 'esp32c3', 'esp32c2']
languages = ['en', 'zh_CN']

google_analytics_id = os.environ.get('CI_GOOGLE_ANALYTICS_ID', None)

project_homepage = 'https://github.com/espressif/esp-idf'

# Custom added feature to allow redirecting old URLs
with open('../page_redirects.txt') as f:
    lines = [re.sub(' +', ' ', line.strip()) for line in f.readlines() if line.strip() != '' and not line.startswith('#')]
    for line in lines:  # check for well-formed entries
        if len(line.split(' ')) != 2:
            raise RuntimeError('Invalid line in page_redirects.txt: %s' % line)
html_redirect_pages = [tuple(line.split(' ')) for line in lines]

html_static_path = ['../_static']


# Callback function for user setup that needs be done after `config-init`-event
# config.idf_target is not available at the initial config stage
def conf_setup(app, config):
    config.add_warnings_content = 'This document is not updated for {} yet, so some of the content may not be correct.'.format(config.idf_target.upper())

    add_warnings_file = '{}/../docs_not_updated/{}.txt'.format(app.confdir, config.idf_target)
    try:
        with open(add_warnings_file) as warning_file:
            config.add_warnings_pages = warning_file.read().splitlines()
    except FileNotFoundError:
        # Not for all target
        pass


user_setup_callback = conf_setup
