"""
    ParallelCluster

    ParallelCluster API  # noqa: E501

    The version of the OpenAPI document: 3.0.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from pcluster_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)

def lazy_import():
    from pcluster_client.model.cloud_formation_stack_status import CloudFormationStackStatus
    from pcluster_client.model.cluster_configuration_structure import ClusterConfigurationStructure
    from pcluster_client.model.cluster_status import ClusterStatus
    from pcluster_client.model.compute_fleet_status import ComputeFleetStatus
    from pcluster_client.model.ec2_instance import EC2Instance
    from pcluster_client.model.tag import Tag
    globals()['CloudFormationStackStatus'] = CloudFormationStackStatus
    globals()['ClusterConfigurationStructure'] = ClusterConfigurationStructure
    globals()['ClusterStatus'] = ClusterStatus
    globals()['ComputeFleetStatus'] = ComputeFleetStatus
    globals()['EC2Instance'] = EC2Instance
    globals()['Tag'] = Tag


class DescribeClusterResponseContent(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
        ('cluster_name',): {
            'regex': {
                'pattern': r'^[a-zA-Z][a-zA-Z0-9-]+$',  # noqa: E501
            },
        },
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'cluster_name': (str,),  # noqa: E501
            'region': (str,),  # noqa: E501
            'version': (str,),  # noqa: E501
            'cloud_formation_stack_status': (CloudFormationStackStatus,),  # noqa: E501
            'cluster_status': (ClusterStatus,),  # noqa: E501
            'cloudformation_stack_arn': (str,),  # noqa: E501
            'creation_time': (datetime,),  # noqa: E501
            'last_updated_time': (datetime,),  # noqa: E501
            'cluster_configuration': (ClusterConfigurationStructure,),  # noqa: E501
            'compute_fleet_status': (ComputeFleetStatus,),  # noqa: E501
            'tags': ([Tag],),  # noqa: E501
            'head_node': (EC2Instance,),  # noqa: E501
            'failure_reason': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'cluster_name': 'clusterName',  # noqa: E501
        'region': 'region',  # noqa: E501
        'version': 'version',  # noqa: E501
        'cloud_formation_stack_status': 'cloudFormationStackStatus',  # noqa: E501
        'cluster_status': 'clusterStatus',  # noqa: E501
        'cloudformation_stack_arn': 'cloudformationStackArn',  # noqa: E501
        'creation_time': 'creationTime',  # noqa: E501
        'last_updated_time': 'lastUpdatedTime',  # noqa: E501
        'cluster_configuration': 'clusterConfiguration',  # noqa: E501
        'compute_fleet_status': 'computeFleetStatus',  # noqa: E501
        'tags': 'tags',  # noqa: E501
        'head_node': 'headNode',  # noqa: E501
        'failure_reason': 'failureReason',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, cluster_name, region, version, cloud_formation_stack_status, cluster_status, cloudformation_stack_arn, creation_time, last_updated_time, cluster_configuration, compute_fleet_status, tags, *args, **kwargs):  # noqa: E501
        """DescribeClusterResponseContent - a model defined in OpenAPI

        Args:
            cluster_name (str): Name of the cluster.
            region (str): AWS region where the cluster is created.
            version (str): ParallelCluster version used to create the cluster.
            cloud_formation_stack_status (CloudFormationStackStatus):
            cluster_status (ClusterStatus):
            cloudformation_stack_arn (str): ARN of the main CloudFormation stack.
            creation_time (datetime): Timestamp representing the cluster creation time.
            last_updated_time (datetime): Timestamp representing the last cluster update time.
            cluster_configuration (ClusterConfigurationStructure):
            compute_fleet_status (ComputeFleetStatus):
            tags ([Tag]): Tags associated with the cluster.

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            head_node (EC2Instance): [optional]  # noqa: E501
            failure_reason (str): Reason of the failure when the stack is in CREATE_FAILED, UPDATE_FAILED or DELETE_FAILED status.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.cluster_name = cluster_name
        self.region = region
        self.version = version
        self.cloud_formation_stack_status = cloud_formation_stack_status
        self.cluster_status = cluster_status
        self.cloudformation_stack_arn = cloudformation_stack_arn
        self.creation_time = creation_time
        self.last_updated_time = last_updated_time
        self.cluster_configuration = cluster_configuration
        self.compute_fleet_status = compute_fleet_status
        self.tags = tags
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
