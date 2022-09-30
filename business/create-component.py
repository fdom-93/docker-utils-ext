from loko_extensions.model.components import Arg, Component, save_extensions, Input, Output, Select, Dynamic


########################## componente stacks info
input_stacks_info = Input(id='input', label='Input', service='stacks_info', to='output')
output_stacks_info = Output(id='output', label='Output')
doc_stacks_info = '''
### Stacks Info\n
With this extension you can view all the info about your stacks.\n
You can then use a function after this block to manipulate and filter all the data you need to use it.
'''
stacks_info = Component(name='Stacks Info', inputs=[input_stacks_info], outputs=[output_stacks_info], description=doc_stacks_info, configured=True)


########################## componente stacks name
input_stacks_name = Input(id='input', label='Input', service='stacks_name', to='output')
output_stacks_name = Output(id='output', label='Output')
doc_stacks_name = '''
### Stacks Name\n
With this extension you can view all the stacks available on your host.
'''
stacks_name = Component(name='Stacks Name', inputs=[input_stacks_name], outputs=[output_stacks_name], description=doc_stacks_name, configured=True)


########################## componente stack inspect
name_stack_inspect = Arg(name='name_stack', label='Stack Name', type='text', helper='Stack name to inspect', value="")
input_stack_inspect = Input(id='input', label='Input', service='stack_inspect', to='output')
output_stack_inspect = Output(id='output', label='Output')
doc_stack_inspect = '''
### Stack Inspect\n
With this extension you can view, giving the name of a stack, all the containers and their configurations related to it.\n
You can use \"Stack Info\" extension to take stack's name.
'''
stack_inspect = Component(name='Stack Inspect', args=[name_stack_inspect], inputs=[input_stack_inspect], outputs=[output_stack_inspect], description=doc_stack_inspect, configured=False)


########################## componente export_stack
id_export = Arg(name='stack_id', label='Stack ID', type='text', helper='Your stack\'s id', value="")

input_export = Input(id='input', label='Input', service='export', to='output')
output_export = Output(id='output', label='Output')
doc_export = '''
### Stack Export\n
With this extension you can export the docker-compose.yml of your stack.\n
You need to configure this block with the id of your stack (you can use \"Stack Info\" extension to take it).
'''
export_stack = Component(name='Export Docker-Compose', args=[id_export], inputs=[input_export], outputs=[output_export], description=doc_export, configured=False)


########################## componente import_stack
name_import = Arg(name='name_new_stack', label='Stack name', type='text', helper='Give a name to your new stack', value="")
# file_import = Arg(name='file_import', label='File Import', type='files', helper='Import your .yml file', value="")

input_import = Input(id='input', label='Input', service='import_stack', to='output')
output_import = Output(id='output', label='Output')
doc_import = '''
### Stack Import\n
With this extension you can import a docker-compose.yml and run on your host.\n
To add your docker-compose.yml file, use \"File Reader\" Input block.
'''
# import_stack = Component(name='Import Docker-Compose', args=[name_import, file_import], inputs=[input_import], outputs=[output_import], description=doc_import, configured=False)
import_stack = Component(name='Import Docker-Compose', args=[name_import], inputs=[input_import], outputs=[output_import], description=doc_import, configured=False)



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



########################## componente Registries
input_registries = Input(id='input', label='Input', service='registries', to='output')
output_registries = Output(id='output', label='Output')
doc_registries = '''
### Registries List\n
With this extension you can view all the registries you are logged in on your host.
'''
registries = Component(name='Registries List', inputs=[input_registries], outputs=[output_registries], description=doc_registries, configured=True)


########################## componente Volumes
input_volumes = Input(id='input', label='Input', service='volumes', to='output')
output_volumes = Output(id='output', label='Output')
doc_volumes = '''
### Volumes List\n
With this extension you can view all the volumes created on your host.
'''
volumes = Component(name='Volumes List', inputs=[input_volumes], outputs=[output_volumes], description=doc_volumes, configured=True)



########################## crea extension
save_extensions([stacks_info, stacks_name, stack_inspect, export_stack, import_stack, list_images, registries, volumes])
