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

input_export = Input(id='input', label='Input', service='export_stack', to='output')
output_export = Output(id='output', label='Output')
doc_export = '''
### Export Docker-Compose\n
With this extension you can export the docker-compose.yml of your stack.\n
You need to configure this block with the id of your stack (you can use \"Stack Info\" extension to take it).
'''
export_stack = Component(name='Export Docker-Compose', args=[id_export], inputs=[input_export], outputs=[output_export], description=doc_export, configured=False)


########################## componente import_stack
name_import = Arg(name='name_new_stack', label='Stack name', type='text', helper='Give a name to your new stack', value="")
file_import = Arg(name='file_import', label='File Import', type='files', helper='Import your .yml file', value="")

input_import = Input(id='input', label='Input', service='import_stack', to='output')
output_import = Output(id='output', label='Output')
doc_import = '''
### Import Docker-Compose\n
With this extension you can run a docker-compose.yml on your host.\n
Give a name to the new stack and select .yml file to import.
'''
import_stack = Component(name='Import Docker-Compose', args=[name_import, file_import], inputs=[input_import], outputs=[output_import], description=doc_import, configured=False)



########################## componente Volumes
input_volumes = Input(id='input', label='Input', service='volumes', to='output')
output_volumes = Output(id='output', label='Output')
doc_volumes = '''
### Volumes List\n
With this extension you can view all the volumes created on your host.
'''
volumes = Component(name='Volumes List', inputs=[input_volumes], outputs=[output_volumes], description=doc_volumes, configured=True)


########################## componente Registries
input_registries = Input(id='input', label='Input', service='registries', to='output')
output_registries = Output(id='output', label='Output')
doc_registries = '''
### Registries List\n
With this extension you can view all the registries you are logged in on your host.
'''
registries = Component(name='Registries List', inputs=[input_registries], outputs=[output_registries], description=doc_registries, configured=True)



########################## componente list-docker-images
select_docker_registry = Select(name="registry_name", label="Registry name", options=[ "registry.livetech.site" ])
search_docker_images = Arg(name='image_name', label='Docker Image Name', type='text', helper='Docker Image name to search', value="")

input_docker_images = Input(id='input', label='Input', service='list-docker-images', to='output')
output_docker_images = Output(id='output', label='Output')
doc_docker_images = '''
### List images in Livetech Docker Registry
With this extension you can see all Docker images pushed on Private Livetech Registry.\n
You need to configure this block with the name of the image you want to search.\n
You don't need to insert the full name of the image, but you can use also search a part of it.\n
*(for example, you can insert \"stor\" to searching \"storage\")*
'''
docker_images = Component(name='List images in Livetech Registry', args=[select_docker_registry, search_docker_images], inputs=[input_docker_images], outputs=[output_docker_images], description=doc_docker_images, configured=False)


########################## componente list-python-lib
select_python_lib = Select(name="pypiserver", label="Pypiserver name", options=[ "distribution.livetech.site" ])
search_python_lib = Arg(name='python_lib', label='Python Library Name', type='text', helper='Image name to search. IMPORTANT: insert the EXACT name of the library', value="")

input_python_lib = Input(id='input', label='Input', service='list-python-lib', to='output')
output_python_lib = Output(id='output', label='Output')
doc_python_lib = '''
### List python libraries in Livetech Pypiserver
With this extension you can see all Python libraries pushed on Private Livetech Pypiserver.\n
You need to configure this block with the name of the python library you want to search.\n
You don't need to insert the full name of the image, but you can use also search a part of it.\n
*(for example, you can insert \"stor\" to searching \"storage\")*
'''
python_lib = Component(name='List libraries in Livetech Pypiserver', args=[select_python_lib, search_python_lib], inputs=[input_python_lib], outputs=[output_python_lib], description=doc_python_lib, configured=False)


########################## crea extensions
save_extensions([stacks_info, stacks_name, stack_inspect, export_stack, import_stack, registries, volumes, docker_images, python_lib])
