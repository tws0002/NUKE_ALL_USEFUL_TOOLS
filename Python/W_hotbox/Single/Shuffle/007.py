#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Alpha
# COLOR: #bababa
# TEXTCOLOR: #111111
#
#----------------------------------------------------------------------------------------------------------

for i in nuke.selectedNodes():
    for channel in ['red','green','blue','alpha']:
        i.knob(channel).setValue('alpha')

    i.knob('tile_color').setValue(4278124287)