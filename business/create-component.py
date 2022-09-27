from loko_extensions.model.components import Arg, Component, save_extensions, Input, Output, Select, Dynamic


select = Select(name="Registry Name", label="Registry name", options=["registry.livetech.site"])
search = Arg(name='Search', type='text', helper='Image name to search', value="")

input = Input(id='input', label='Input', service='list-images', to='output')
output = Output(id='output', label='Output')
doc = '''
### List images in Livetech Registry
With this extension you can see all Docker images pushed on Private Livetech Registry.\n
You need to configure this block with the name of the image you want to search.\n
You don't need to insert the full name of the image, but you can use also search a part of it.\n
*(for example, you can insert \"stor\" to searching \"storage\"*
'''
list_images = Component(name='List images in Livetech Registry', args=[select, search], inputs=[input], outputs=[output], description=doc, configured=false)

save_extensions([list_images])
