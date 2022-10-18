from loko_extensions.model.components import Arg, Component, save_extensions, Input, Output, Select, AsyncSelect


########################## componente stacks name
input_stacks_name = Input(id='input', label='Input', service='stacks_name', to='output')
output_stacks_name = Output(id='output', label='Output')
doc_stacks_name = '''
### Stacks Name\n
With this extension you can view all the stacks available on your host.
'''
stacks_name = Component(name='Stacks Name', inputs=[input_stacks_name], outputs=[output_stacks_name],
                        description=doc_stacks_name, group="Docker-Utils Info", configured=True,
                        trigger=True, icon='RiInformationFill')


########################## componente stack_id
name_stack_id = AsyncSelect(name='stack_name', label='Stack Name',
                            url='http://localhost:9999/routes/docker-utils-ext/stacks_name_list',
                            helper='Name of the stack to be convert to its ID',
                            required=True)
input_stack_id = Input(id='input', label='Input', service='stack_id', to='output')
output_stack_id = Output(id='output', label='Output')
doc_stack_id = '''
### Stacks ID\n
With this extension you can view the ID of a Stack.
'''
stack_id = Component(name='Stacks ID', args=[name_stack_id], inputs=[input_stack_id], outputs=[output_stack_id],
                     description=doc_stack_id, group="Docker-Utils Info", configured=False,
                     trigger=True, icon='RiInformationFill')


########################## componente stacks_info
input_stacks_info = Input(id='input', label='Input', service='stacks_info', to='output')
output_stacks_info = Output(id='output', label='Output')
doc_stacks_info = '''
### Stacks Info\n
With this extension you can view all the info about your stacks.\n
You can then use a function after this block to manipulate and filter all the data you need to use it.
'''
stacks_info = Component(name='Stacks Info', inputs=[input_stacks_info], outputs=[output_stacks_info],
                        description=doc_stacks_info, group="Docker-Utils Info", configured=True,
                        icon='RiInformationFill')


########################## componente container_id
name_stack_cont_id = AsyncSelect(name='stack_name', label='Stack Name',
                                 url='http://localhost:9999/routes/docker-utils-ext/stacks_name_list',
                                 helper='Stack name of your container',
                                 required=True)
name_container_id = Arg(name='container_name', label='Container Name', type='text',
                        helper='Name of the container to be converted to its ID', value="", required=True)
input_container_id = Input(id='input', label='Input', service='container_id', to='output')
output_container_id = Output(id='output', label='Output')
doc_container_id = '''
### Container ID\n
With this extension you can view the ID of a Container.
'''
container_id = Component(name='Container ID', args=[name_stack_cont_id, name_container_id], inputs=[input_container_id],
                         outputs=[output_container_id], description=doc_container_id, group="Docker-Utils Info",
                         configured=False, trigger=True, icon='RiInformationFill')


########################## componente containers_info
input_containers_info = Input(id='input', label='Input', service='containers_info', to='output')
output_containers_info = Output(id='output', label='Output')
doc_containers_info = '''
### Containers Info\n
With this extension you can view all the containers on the host.\n
You can then use a function after this block to manipulate and filter all the data you need to use it.
'''
containers_info = Component(name='Containers Info', inputs=[input_containers_info], outputs=[output_containers_info],
                            description=doc_containers_info, group="Docker-Utils Info", configured=True,
                            trigger=True, icon='RiInformationFill')


########################## componente stack inspect
name_stack_inspect = AsyncSelect(name='name_stack', label='Stack Name',
                                 url='http://localhost:9999/routes/docker-utils-ext/stacks_name_list',
                                 helper='Stack name to inspect', required=True)
input_stack_inspect = Input(id='input', label='Input', service='stack_inspect', to='output')
output_stack_inspect = Output(id='output', label='Output')
doc_stack_inspect = '''
### Stack Inspect\n
With this extension you can view all the containers and their configurations related to a Stack.\n
'''
stack_inspect = Component(name='Stack Inspect', args=[name_stack_inspect], inputs=[input_stack_inspect],
                          outputs=[output_stack_inspect], description=doc_stack_inspect, group="Docker-Utils Info",
                          configured=False, trigger=True, icon='RiInformationFill')


########################## componente export_stack
name_export = AsyncSelect(name='stack_name', label='Stack Name',
                          url='http://localhost:9999/routes/docker-utils-ext/stacks_name_list',
                          helper='Stack\'s name to export', required=True)
input_export = Input(id='input', label='Input', service='export_stack', to='output')
output_export = Output(id='output', label='Output')
doc_export = '''
### Export Docker-Compose\n
With this extension you can export the docker-compose.yml of your stack.\n
You can then use a File Writer to save it on the host.
'''
export_stack = Component(name='Export Docker-Compose', args=[name_export], inputs=[input_export], outputs=[output_export],
                         description=doc_export, group="Docker-Utils Import/Export", configured=False,
                         trigger=True, icon='RiUploadFill')


########################## componente import_stack
name_import = Arg(name='name_new_stack', label='Stack name', type='text', helper='Give a name to your new stack',
                  value="", required=True)
file_import = Arg(name='file_import', label='File Import', type='files', helper='Import your .yml file',
                  value="", required=True)

input_import = Input(id='input', label='Input', service='import_stack', to='output')
output_import = Output(id='output', label='Output')
doc_import = '''
### Import Docker-Compose\n
With this extension you can run a docker-compose.yml on your host.\n
Give a name to the new stack and select .yml file to import.
'''
import_stack = Component(name='Import Docker-Compose', args=[name_import, file_import], inputs=[input_import],
                         outputs=[output_import], description=doc_import, group="Docker-Utils Import/Export",
                         configured=False, trigger=True, icon='RiDownload2Fill')


########################## componente stack pause
name_stack_pause = AsyncSelect(name='stack_name_pause', label='Stack Name',
                               url='http://localhost:9999/routes/docker-utils-ext/stacks_name_list',
                               helper='Stack Name to pause', required=True)
input_stack_pause = Input(id='input', label='Input', service='stack_pause', to='output')
output_stack_pause = Output(id='output', label='Output')
doc_stack_pause = '''
### Stack Pause\n
With this extension you can pause all the containers related to a Stack.\n
'''
stack_pause = Component(name='Stack Pause', args=[name_stack_pause], inputs=[input_stack_pause],
                        outputs=[output_stack_pause], description=doc_stack_pause, group="Docker-Utils Pause/Unpause",
                        configured=False, trigger=True, icon='RiPauseCircleFill')


########################## componente stack unpause
name_stack_unpause = AsyncSelect(name='stack_name_unpause', label='Stack Name',
                                 url='http://localhost:9999/routes/docker-utils-ext/stacks_name_list',
                                 helper='Stack Name to unpause', required=True)
input_stack_unpause = Input(id='input', label='Input', service='stack_unpause', to='output')
output_stack_unpause = Output(id='output', label='Output')
doc_stack_unpause = '''
### Stack Unpause\n
With this extension you can unpause all the containers related to a Stack.\n
'''
stack_unpause = Component(name='Stack Unpause', args=[name_stack_unpause], inputs=[input_stack_unpause],
                          outputs=[output_stack_unpause], description=doc_stack_unpause,
                          group="Docker-Utils Pause/Unpause", configured=False, trigger=True, icon='RiPlayCircleFill')


########################## componente container pause
name_stack_cont_pause = AsyncSelect(name='stack_cont_name_pause', label='Stack Name',
                                    url='http://localhost:9999/routes/docker-utils-ext/stacks_name_list',
                                    helper='The Stack Name of the container to pause', required=True)
name_container_pause = Arg(name='container_name_pause', label='Container Name', type='text',
                           helper='Container Name to pause', value="", required=True)
input_container_pause = Input(id='input', label='Input', service='container_pause', to='output')
output_container_pause = Output(id='output', label='Output')
doc_container_pause = '''
### Container Pause\n
With this extension you can pause a specific container in a Stack.\n
You can use \"Stack Inspect\" or \"Containers Info\" extensions to take container's Name.
'''
container_pause = Component(name='Container Pause', args=[name_stack_cont_pause, name_container_pause],
                            inputs=[input_container_pause], outputs=[output_container_pause],
                            description=doc_container_pause, group="Docker-Utils Pause/Unpause", configured=False,
                            trigger=True, icon='RiPauseCircleFill')


########################## componente container unpause
name_stack_cont_unpause = AsyncSelect(name='stack_cont_name_unpause', label='Stack Name',
                                      url='http://localhost:9999/routes/docker-utils-ext/stacks_name_list',
                                      helper='The Stack Name of the container to unpause', required=True)
name_container_unpause = Arg(name='container_name_unpause', label='Container Name', type='text',
                             helper='Container Name to unpause', value="", required=True)
input_container_unpause = Input(id='input', label='Input', service='container_unpause', to='output')
output_container_unpause = Output(id='output', label='Output')
doc_container_unpause = '''
### Container Unpause\n
With this extension you can unpause a specific container in a Stack.\n
You can use \"Stack Inspect\" or \"Containers Info\" extensions to take container's Name.
'''
container_unpause = Component(name='Container Unpause', args=[name_stack_cont_unpause, name_container_unpause],
                              inputs=[input_container_unpause], outputs=[output_container_unpause],
                              description=doc_container_unpause, group="Docker-Utils Pause/Unpause",
                              configured=False, trigger=True, icon='RiPlayCircleFill')


########################## componente stack delete
name_stack_delete = AsyncSelect(name='stack_name_delete', label='Stack Name',
                                url='http://localhost:9999/routes/docker-utils-ext/stacks_name_list',
                                helper='Stack Name to delete', required=True)
input_stack_delete = Input(id='input', label='Input', service='stack_delete', to='output')
output_stack_delete = Output(id='output', label='Output')
doc_stack_delete = '''
### Stack Delete\n
With this extension you can delete all the containers in a Stack.\n
'''
stack_delete = Component(name='Stack Delete', args=[name_stack_delete], inputs=[input_stack_delete],
                         outputs=[output_stack_delete], description=doc_stack_delete, group="Docker-Utils Delete",
                         configured=False, trigger=True, icon='RiDeleteBin2Fill')


########################## componente container delete
name_stack_cont_delete = AsyncSelect(name='stack_cont_name_delete', label='Stack Name',
                                     url='http://localhost:9999/routes/docker-utils-ext/stacks_name_list',
                                     helper='The Stack Name of the container to delete',
                                     required=True)
name_container_delete = Arg(name='container_name_delete', label='Container Name', type='text',
                            helper='Container Name to delete', value="", required=True)
input_container_delete = Input(id='input', label='Input', service='container_delete', to='output')
output_container_delete = Output(id='output', label='Output')
doc_container_delete = '''
### Container Delete\n
With this extension you can delete a specific container in a Stack.\n
You can use \"Stack Inspect\" or \"Containers Info\" extensions to take container's Name.
'''
container_delete = Component(name='Container Delete', args=[name_stack_cont_delete, name_container_delete],
                             inputs=[input_container_delete], outputs=[output_container_delete],
                             description=doc_container_delete, group="Docker-Utils Delete", configured=False,
                             trigger=True, icon='RiDeleteBin2Fill')


########################## componente Volumes
input_volumes = Input(id='input', label='Input', service='volumes', to='output')
output_volumes = Output(id='output', label='Output')
doc_volumes = '''
### Volumes List\n
With this extension you can view all the volumes created on your host.
'''
volumes = Component(name='Volumes List', inputs=[input_volumes], outputs=[output_volumes], description=doc_volumes,
                    group="Docker-Utils Host info", configured=True, trigger=True, icon='RiHomeFill')


########################## componente Registries
input_registries = Input(id='input', label='Input', service='registries', to='output')
output_registries = Output(id='output', label='Output')
doc_registries = '''
### Registries List\n
With this extension you can view all the registries you are logged in on your host.
'''
registries = Component(name='Registries List', inputs=[input_registries], outputs=[output_registries],
                       description=doc_registries, group="Docker-Utils Host info", configured=True,
                       trigger=True, icon='RiHomeFill')


########################## componente search_docker_images
select_docker_registry = Select(name="registry_name", label="Registry name", options=["registry.livetech.site"],
                                required=True)
search_docker_images = Arg(name='image_name', label='Docker Image Name', type='text',
                           helper='Docker Image name to search', value="", required=True)
input_docker_images = Input(id='input', label='Input', service='search_docker_images', to='output')
output_docker_images = Output(id='output', label='Output')
doc_docker_images = '''
### Search images in Private Docker Registry
With this extension you can see all Docker image's versions pushed on Private Registry.\n
You need to configure this block with the name of the image you want to search.\n
You don't need to insert the full name of the image, but you can use also search a part of it.\n
*(for example, you can insert \"stor\" to searching \"storage\")*
'''
docker_images = Component(name='Search in Private Docker Registry', args=[select_docker_registry, search_docker_images],
                          inputs=[input_docker_images], outputs=[output_docker_images], description=doc_docker_images,
                          group="Docker-Utils Registry/Pypiserver", configured=False,
                          trigger=True, icon='RiFileSearchFill')


########################## componente search_python_lib
select_python_lib = Select(name="pypiserver", label="Pypiserver name", options=["distribution.livetech.site"],
                           required=True)
search_python_lib = Arg(name='python_lib', label='Python Library Name', type='text',
                        helper='Image name to search. IMPORTANT: insert the EXACT name of the library',
                        value="", required=True)
input_python_lib = Input(id='input', label='Input', service='search_python_lib', to='output')
output_python_lib = Output(id='output', label='Output')
doc_python_lib = '''
### Search libraries in Private Pypiserver
With this extension you can see all Python library's versions pushed on Private Pypiserver.\n
You need to configure this block with the name of the python library you want to search.\n
You MUST insert the full name of the python library!
'''
python_lib = Component(name='Search in Private Pypiserver', args=[select_python_lib, search_python_lib],
                       inputs=[input_python_lib], outputs=[output_python_lib], description=doc_python_lib,
                       group="Docker-Utils Registry/Pypiserver", configured=False, trigger=True, icon='RiFileSearchFill')




########################## crea extensions
save_extensions([stacks_name, stack_id, stacks_info, container_id, containers_info, stack_inspect, export_stack,
                import_stack, stack_pause, stack_unpause, container_pause, container_unpause,
                 stack_delete, container_delete, registries, volumes, docker_images, python_lib])
