# Copyright 2024 Kinsey Moore (kinsey.moore@oarcorp.com)
#
# This file is licensed under 2-clause BSD. See the LICENSE file for the full text.
#

from __future__ import print_function

rtems_version = "6"

try:
    import rtems_waf.rtems as rtems
    import rtems_waf.rtems_bsd as rtems_bsd
except:
    print('error: no rtems_waf git submodule; see README')
    import sys
    sys.exit(1)

def init(ctx):
    rtems.init(ctx, version = rtems_version, long_commands = True)

def bsp_configure(conf, arch_bsp):
    rtems_bsd.bsp_configure(conf, arch_bsp, mandatory = False)

def options(opt):
    rtems.options(opt)
    rtems_bsd.options(opt)

def configure(conf):
    rtems.configure(conf, bsp_configure = bsp_configure)

def build(bld):
    rtems.build(bld)
    bld.env.CFLAGS += ['-O2','-g']
    bld(features = 'c cprogram',
        target = 'application.exe',
        source = ['application.c'])

def rebuild(ctx):
    import waflib.Options
    waflib.Options.commands.extend(['clean', 'build'])

def tags(ctx):
    ctx.exec_command('etags $(find . -name \*.[sSch])', shell = True)
