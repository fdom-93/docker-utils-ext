from loko_extensions.model.components import Arg, Component, save_extensions, Input, Output, Select, Dynamic


########################## componente stacks
input_stacks = Input(id='input', label='Input', service='stacks', to='output')
output_stacks = Output(id='output', label='Output')
doc_stacks = '''
### Stacks Info\n
With this extension you can view all the info about your stacks.\n
You can then use a function after this block to manipulate and filter all the data you need to use it.
'''
stacks = Component(name='Stacks Info', inputs=[input_stacks], outputs=[output_stacks], description=doc_stacks, configured=True)


########################## componente export
id_export = Arg(name='stack_id', label='Stack ID', type='text', helper='Your stack\'s id', value="")

input_export = Input(id='input', label='Input', service='export', to='output')
output_export = Output(id='output', label='Output')
doc_export = '''
### Stack Export\n
With this extension you can export the docker-compose.yml of your stack.\n
You need to configure this block with the id of your stack (you can use \"Stack Info\" extension to take it).
'''
export = Component(name='Export Docker-Compose', args=[id_export], inputs=[input_export], outputs=[output_export], description=doc_export, configured=False)


########################## componente list-images

select_list_images = Select(name="registry_name", label="Registry name", options=[ "registry.livetech.site" ])
search_list_images = Arg(name='image_name', label='Image Name', type='text', helper='Image name to search', value="")

input_list_images = Input(id='input', label='Input', service='list-images', to='output')
output_list_images = Output(id='output', label='Output')
doc_list_images = '''
### List images in Livetech Registry
With this extension you can see all Docker images pushed on Private Livetech Registry.\n
You need to configure this block with the name of the image you want to search.\n
You don't need to insert the full name of the image, but you can use also search a part of it.\n
*(for example, you can insert \"stor\" to searching \"storage\")*
'''
list_images = Component(name='List images in Livetech Registry', args=[select_list_images, search_list_images], inputs=[input_list_images], outputs=[output_list_images], description=doc_list_images, configured=False)




########################## crea extension
save_extensions([stacks, export, list_images])
