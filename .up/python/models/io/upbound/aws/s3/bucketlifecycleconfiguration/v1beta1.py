# generated by datamodel-codegen:
#   filename:  workdir/s3_aws_upbound_io_v1beta1_bucketlifecycleconfiguration.yaml

from __future__ import annotations

from enum import Enum
from typing import Dict, List, Optional

from pydantic import AwareDatetime, BaseModel, Field

from .....k8s.apimachinery.pkg.apis.meta import v1


class DeletionPolicy(Enum):
    Orphan = 'Orphan'
    Delete = 'Delete'


class Resolution(Enum):
    Required = 'Required'
    Optional = 'Optional'


class Resolve(Enum):
    Always = 'Always'
    IfNotPresent = 'IfNotPresent'


class Policy(BaseModel):
    resolution: Optional[Resolution] = 'Required'
    """
    Resolution specifies whether resolution of this reference is required.
    The default is 'Required', which means the reconcile will fail if the
    reference cannot be resolved. 'Optional' means this reference will be
    a no-op if it cannot be resolved.
    """
    resolve: Optional[Resolve] = None
    """
    Resolve specifies when this reference should be resolved. The default
    is 'IfNotPresent', which will attempt to resolve the reference only when
    the corresponding field is not present. Use 'Always' to resolve the
    reference on every reconcile.
    """


class BucketRef(BaseModel):
    name: str
    """
    Name of the referenced object.
    """
    policy: Optional[Policy] = None
    """
    Policies for referencing.
    """


class BucketSelector(BaseModel):
    matchControllerRef: Optional[bool] = None
    """
    MatchControllerRef ensures an object with the same controller reference
    as the selecting object is selected.
    """
    matchLabels: Optional[Dict[str, str]] = None
    """
    MatchLabels ensures an object with matching labels is selected.
    """
    policy: Optional[Policy] = None
    """
    Policies for selection.
    """


class AbortIncompleteMultipartUploadItem(BaseModel):
    daysAfterInitiation: Optional[float] = None
    """
    Number of days after which Amazon S3 aborts an incomplete multipart upload.
    """


class ExpirationItem(BaseModel):
    date: Optional[str] = None
    """
    Date objects are transitioned to the specified storage class. The date value must be in RFC3339 full-date format e.g. 2023-08-22.
    """
    days: Optional[float] = None
    """
    Number of days after creation when objects are transitioned to the specified storage class. The value must be a positive integer. If both days and date are not specified, defaults to 0. Valid values depend on storage_class, see Transition objects using Amazon S3 Lifecycle for more details.
    """
    expiredObjectDeleteMarker: Optional[bool] = None
    """
    Indicates whether Amazon S3 will remove a delete marker with no noncurrent versions. If set to true, the delete marker will be expired; if set to false the policy takes no action.
    """


class AndItem(BaseModel):
    objectSizeGreaterThan: Optional[float] = None
    """
    Minimum object size (in bytes) to which the rule applies.
    """
    objectSizeLessThan: Optional[float] = None
    """
    Maximum object size (in bytes) to which the rule applies.
    """
    prefix: Optional[str] = None
    """
    Prefix identifying one or more objects to which the rule applies.
    """
    tags: Optional[Dict[str, str]] = None
    """
    Key-value map of resource tags. All of these tags must exist in the object's tag set in order for the rule to apply.
    """


class TagItem(BaseModel):
    key: Optional[str] = None
    """
    Name of the object key.
    """
    value: Optional[str] = None
    """
    Value of the tag.
    """


class FilterItem(BaseModel):
    and_: Optional[List[AndItem]] = Field(None, alias='and')
    """
    Configuration block used to apply a logical AND to two or more predicates. See below. The Lifecycle Rule will apply to any object matching all the predicates configured inside the and block.
    """
    objectSizeGreaterThan: Optional[str] = None
    """
    Minimum object size (in bytes) to which the rule applies.
    """
    objectSizeLessThan: Optional[str] = None
    """
    Maximum object size (in bytes) to which the rule applies.
    """
    prefix: Optional[str] = None
    """
    Prefix identifying one or more objects to which the rule applies. Defaults to an empty string ("") if not specified.
    """
    tag: Optional[List[TagItem]] = None
    """
    Configuration block for specifying a tag key and value. See below.
    """


class NoncurrentVersionExpirationItem(BaseModel):
    newerNoncurrentVersions: Optional[str] = None
    """
    Number of noncurrent versions Amazon S3 will retain. Must be a non-zero positive integer.
    """
    noncurrentDays: Optional[float] = None
    """
    Number of days an object is noncurrent before Amazon S3 can perform the associated action.
    """


class NoncurrentVersionTransitionItem(BaseModel):
    newerNoncurrentVersions: Optional[str] = None
    """
    Number of noncurrent versions Amazon S3 will retain. Must be a non-zero positive integer.
    """
    noncurrentDays: Optional[float] = None
    """
    Number of days an object is noncurrent before Amazon S3 can perform the associated action.
    """
    storageClass: Optional[str] = None
    """
    Class of storage used to store the object. Valid Values: GLACIER, STANDARD_IA, ONEZONE_IA, INTELLIGENT_TIERING, DEEP_ARCHIVE, GLACIER_IR.
    """


class TransitionItem(BaseModel):
    date: Optional[str] = None
    """
    Date objects are transitioned to the specified storage class. The date value must be in RFC3339 full-date format e.g. 2023-08-22.
    """
    days: Optional[float] = None
    """
    Number of days after creation when objects are transitioned to the specified storage class. The value must be a positive integer. If both days and date are not specified, defaults to 0. Valid values depend on storage_class, see Transition objects using Amazon S3 Lifecycle for more details.
    """
    storageClass: Optional[str] = None
    """
    Class of storage used to store the object. Valid Values: GLACIER, STANDARD_IA, ONEZONE_IA, INTELLIGENT_TIERING, DEEP_ARCHIVE, GLACIER_IR.
    """


class RuleItem(BaseModel):
    abortIncompleteMultipartUpload: Optional[
        List[AbortIncompleteMultipartUploadItem]
    ] = None
    """
    Configuration block that specifies the days since the initiation of an incomplete multipart upload that Amazon S3 will wait before permanently removing all parts of the upload. See below.
    """
    expiration: Optional[List[ExpirationItem]] = None
    """
    Configuration block that specifies the expiration for the lifecycle of the object in the form of date, days and, whether the object has a delete marker. See below.
    """
    filter: Optional[List[FilterItem]] = None
    """
    Configuration block used to identify objects that a Lifecycle Rule applies to. See below. If not specified, the rule will default to using prefix.
    """
    id: Optional[str] = None
    """
    Unique identifier for the rule. The value cannot be longer than 255 characters.
    """
    noncurrentVersionExpiration: Optional[List[NoncurrentVersionExpirationItem]] = None
    """
    Configuration block that specifies when noncurrent object versions expire. See below.
    """
    noncurrentVersionTransition: Optional[List[NoncurrentVersionTransitionItem]] = None
    """
    Set of configuration blocks that specify the transition rule for the lifecycle rule that describes when noncurrent objects transition to a specific storage class. See below.
    """
    prefix: Optional[str] = None
    """
    DEPRECATED Use filter instead. This has been deprecated by Amazon S3. Prefix identifying one or more objects to which the rule applies. Defaults to an empty string ("") if filter is not specified.
    """
    status: Optional[str] = None
    """
    Whether the rule is currently being applied. Valid values: Enabled or Disabled.
    """
    transition: Optional[List[TransitionItem]] = None
    """
    Set of configuration blocks that specify when an Amazon S3 object transitions to a specified storage class. See below.
    """


class ForProvider(BaseModel):
    bucket: Optional[str] = None
    """
    Name of the source S3 bucket you want Amazon S3 to monitor.
    """
    bucketRef: Optional[BucketRef] = None
    """
    Reference to a Bucket in s3 to populate bucket.
    """
    bucketSelector: Optional[BucketSelector] = None
    """
    Selector for a Bucket in s3 to populate bucket.
    """
    expectedBucketOwner: Optional[str] = None
    """
    Account ID of the expected bucket owner. If the bucket is owned by a different account, the request will fail with an HTTP 403 (Access Denied) error.
    """
    region: str
    """
    Region is the region you'd like your resource to be created in.
    """
    rule: Optional[List[RuleItem]] = None
    """
    List of configuration blocks describing the rules managing the replication. See below.
    """


class InitProvider(BaseModel):
    bucket: Optional[str] = None
    """
    Name of the source S3 bucket you want Amazon S3 to monitor.
    """
    bucketRef: Optional[BucketRef] = None
    """
    Reference to a Bucket in s3 to populate bucket.
    """
    bucketSelector: Optional[BucketSelector] = None
    """
    Selector for a Bucket in s3 to populate bucket.
    """
    expectedBucketOwner: Optional[str] = None
    """
    Account ID of the expected bucket owner. If the bucket is owned by a different account, the request will fail with an HTTP 403 (Access Denied) error.
    """
    rule: Optional[List[RuleItem]] = None
    """
    List of configuration blocks describing the rules managing the replication. See below.
    """


class ManagementPolicy(Enum):
    Observe = 'Observe'
    Create = 'Create'
    Update = 'Update'
    Delete = 'Delete'
    LateInitialize = 'LateInitialize'
    field_ = '*'


class ProviderConfigRef(BaseModel):
    name: str
    """
    Name of the referenced object.
    """
    policy: Optional[Policy] = None
    """
    Policies for referencing.
    """


class ConfigRef(BaseModel):
    name: str
    """
    Name of the referenced object.
    """
    policy: Optional[Policy] = None
    """
    Policies for referencing.
    """


class Metadata(BaseModel):
    annotations: Optional[Dict[str, str]] = None
    """
    Annotations are the annotations to be added to connection secret.
    - For Kubernetes secrets, this will be used as "metadata.annotations".
    - It is up to Secret Store implementation for others store types.
    """
    labels: Optional[Dict[str, str]] = None
    """
    Labels are the labels/tags to be added to connection secret.
    - For Kubernetes secrets, this will be used as "metadata.labels".
    - It is up to Secret Store implementation for others store types.
    """
    type: Optional[str] = None
    """
    Type is the SecretType for the connection secret.
    - Only valid for Kubernetes Secret Stores.
    """


class PublishConnectionDetailsTo(BaseModel):
    configRef: Optional[ConfigRef] = Field(
        default_factory=lambda: ConfigRef.model_validate({'name': 'default'})
    )
    """
    SecretStoreConfigRef specifies which secret store config should be used
    for this ConnectionSecret.
    """
    metadata: Optional[Metadata] = None
    """
    Metadata is the metadata for connection secret.
    """
    name: str
    """
    Name is the name of the connection secret.
    """


class WriteConnectionSecretToRef(BaseModel):
    name: str
    """
    Name of the secret.
    """
    namespace: str
    """
    Namespace of the secret.
    """


class Spec(BaseModel):
    deletionPolicy: Optional[DeletionPolicy] = 'Delete'
    """
    DeletionPolicy specifies what will happen to the underlying external
    when this managed resource is deleted - either "Delete" or "Orphan" the
    external resource.
    This field is planned to be deprecated in favor of the ManagementPolicies
    field in a future release. Currently, both could be set independently and
    non-default values would be honored if the feature flag is enabled.
    See the design doc for more information: https://github.com/crossplane/crossplane/blob/499895a25d1a1a0ba1604944ef98ac7a1a71f197/design/design-doc-observe-only-resources.md?plain=1#L223
    """
    forProvider: ForProvider
    initProvider: Optional[InitProvider] = None
    """
    THIS IS A BETA FIELD. It will be honored
    unless the Management Policies feature flag is disabled.
    InitProvider holds the same fields as ForProvider, with the exception
    of Identifier and other resource reference fields. The fields that are
    in InitProvider are merged into ForProvider when the resource is created.
    The same fields are also added to the terraform ignore_changes hook, to
    avoid updating them after creation. This is useful for fields that are
    required on creation, but we do not desire to update them after creation,
    for example because of an external controller is managing them, like an
    autoscaler.
    """
    managementPolicies: Optional[List[ManagementPolicy]] = ['*']
    """
    THIS IS A BETA FIELD. It is on by default but can be opted out
    through a Crossplane feature flag.
    ManagementPolicies specify the array of actions Crossplane is allowed to
    take on the managed and external resources.
    This field is planned to replace the DeletionPolicy field in a future
    release. Currently, both could be set independently and non-default
    values would be honored if the feature flag is enabled. If both are
    custom, the DeletionPolicy field will be ignored.
    See the design doc for more information: https://github.com/crossplane/crossplane/blob/499895a25d1a1a0ba1604944ef98ac7a1a71f197/design/design-doc-observe-only-resources.md?plain=1#L223
    and this one: https://github.com/crossplane/crossplane/blob/444267e84783136daa93568b364a5f01228cacbe/design/one-pager-ignore-changes.md
    """
    providerConfigRef: Optional[ProviderConfigRef] = Field(
        default_factory=lambda: ProviderConfigRef.model_validate({'name': 'default'})
    )
    """
    ProviderConfigReference specifies how the provider that will be used to
    create, observe, update, and delete this managed resource should be
    configured.
    """
    publishConnectionDetailsTo: Optional[PublishConnectionDetailsTo] = None
    """
    PublishConnectionDetailsTo specifies the connection secret config which
    contains a name, metadata and a reference to secret store config to
    which any connection details for this managed resource should be written.
    Connection details frequently include the endpoint, username,
    and password required to connect to the managed resource.
    """
    writeConnectionSecretToRef: Optional[WriteConnectionSecretToRef] = None
    """
    WriteConnectionSecretToReference specifies the namespace and name of a
    Secret to which any connection details for this managed resource should
    be written. Connection details frequently include the endpoint, username,
    and password required to connect to the managed resource.
    This field is planned to be replaced in a future release in favor of
    PublishConnectionDetailsTo. Currently, both could be set independently
    and connection details would be published to both without affecting
    each other.
    """


class AtProvider(BaseModel):
    bucket: Optional[str] = None
    """
    Name of the source S3 bucket you want Amazon S3 to monitor.
    """
    expectedBucketOwner: Optional[str] = None
    """
    Account ID of the expected bucket owner. If the bucket is owned by a different account, the request will fail with an HTTP 403 (Access Denied) error.
    """
    id: Optional[str] = None
    """
    and status)
    """
    rule: Optional[List[RuleItem]] = None
    """
    List of configuration blocks describing the rules managing the replication. See below.
    """


class Condition(BaseModel):
    lastTransitionTime: AwareDatetime
    """
    LastTransitionTime is the last time this condition transitioned from one
    status to another.
    """
    message: Optional[str] = None
    """
    A Message containing details about this condition's last transition from
    one status to another, if any.
    """
    observedGeneration: Optional[int] = None
    """
    ObservedGeneration represents the .metadata.generation that the condition was set based upon.
    For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date
    with respect to the current state of the instance.
    """
    reason: str
    """
    A Reason for this condition's last transition from one status to another.
    """
    status: str
    """
    Status of this condition; is it currently True, False, or Unknown?
    """
    type: str
    """
    Type of this condition. At most one of each condition type may apply to
    a resource at any point in time.
    """


class Status(BaseModel):
    atProvider: Optional[AtProvider] = None
    conditions: Optional[List[Condition]] = None
    """
    Conditions of the resource.
    """
    observedGeneration: Optional[int] = None
    """
    ObservedGeneration is the latest metadata.generation
    which resulted in either a ready state, or stalled due to error
    it can not recover from without human intervention.
    """


class BucketLifecycleConfiguration(BaseModel):
    apiVersion: Optional[str] = None
    """
    APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    """
    kind: Optional[str] = None
    """
    Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    metadata: Optional[v1.ObjectMeta] = None
    """
    Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
    """
    spec: Spec
    """
    BucketLifecycleConfigurationSpec defines the desired state of BucketLifecycleConfiguration
    """
    status: Optional[Status] = None
    """
    BucketLifecycleConfigurationStatus defines the observed state of BucketLifecycleConfiguration.
    """


class BucketLifecycleConfigurationList(BaseModel):
    apiVersion: Optional[str] = None
    """
    APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    """
    items: List[BucketLifecycleConfiguration]
    """
    List of bucketlifecycleconfigurations. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md
    """
    kind: Optional[str] = None
    """
    Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    metadata: Optional[v1.ListMeta] = None
    """
    Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """