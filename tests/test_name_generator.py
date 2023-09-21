import docker_names

def test_name_formats():
	random_name = docker_names.get_random_name(retry=0)
	assert isinstance(random_name, str)
	assert '_' in random_name
	
def test_name_retry():
	random_name = docker_names.get_random_name(retry=1)
	assert int(random_name[-1]) in range(11)
