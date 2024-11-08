from crossplane.function import resource
from crossplane.function.proto.v1 import run_function_pb2 as fnv1
from model.io.k8s.apimachinery.pkg.apis.meta import v1 as metav1
from model.com.example.platform.xstoragebucket import v1alpha1
from model.io.upbound.aws.s3.bucket import v1beta1 as bucketv1beta1
from model.io.upbound.aws.s3.bucketacl import v1beta1 as aclv1beta1
from model.io.upbound.aws.s3.bucketversioning import v1beta1 as verv1beta1
from model.io.upbound.aws.s3.bucketserversideencryptionconfiguration import v1beta1 as ssev1beta1
from model.io.upbound.aws.s3.bucketownershipcontrols import v1beta1 as bocv1beta1
from model.io.upbound.aws.s3.bucketpublicaccessblock import v1beta1 as pabv1beta1

def compose(req: fnv1.RunFunctionRequest, rsp: fnv1.RunFunctionResponse):
    observed_xr = v1alpha1.XStorageBucket(**req.observed.composite.resource)
    xr_name = observed_xr.metadata.name
    bucket_name = xr_name + "-bucket"
    params = observed_xr.spec.parameters

    bucket = bucketv1beta1.Bucket(
        apiVersion="s3.aws.upbound.io/v1beta1",
        kind="Bucket",
        metadata=metav1.ObjectMeta(
            name=bucket_name,
        ),
        spec=bucketv1beta1.Spec(
            forProvider=bucketv1beta1.ForProvider(
                region=params.region,
            ),
        ),
    )
    resource.update(rsp.desired.resources[bucket.metadata.name], bucket)

    acl = aclv1beta1.BucketACL(
        apiVersion="s3.aws.upbound.io/v1beta1",
        kind="BucketACL",
        metadata=metav1.ObjectMeta(
            name=xr_name + "-acl",
        ),
        spec=aclv1beta1.Spec(
            forProvider=aclv1beta1.ForProvider(
                region=params.region,
                bucketRef=aclv1beta1.BucketRef(
                    name = bucket_name,
                ),
                acl=params.acl,
            ),
        ),
    )
    resource.update(rsp.desired.resources[acl.metadata.name], acl)

    boc = bocv1beta1.BucketOwnershipControls(
        apiVersion="s3.aws.upbound.io/v1beta1",
        kind="BucketOwnershipControls",
        metadata=metav1.ObjectMeta(
            name=xr_name + "-boc",
        ),
        spec=bocv1beta1.Spec(
            forProvider=bocv1beta1.ForProvider(
                region=params.region,
                bucketRef=bocv1beta1.BucketRef(
                    name = bucket_name,
                ),
                rule=[
                    bocv1beta1.RuleItem(
                        objectOwnership="BucketOwnerPreferred",
                    ),
                ],
            )
        )
    )
    resource.update(rsp.desired.resources[boc.metadata.name], boc)

    pab = pabv1beta1.BucketPublicAccessBlock(
        apiVersion="s3.aws.upbound.io/v1beta1",
        kind="BucketPublicAccessBlock",
        metadata=metav1.ObjectMeta(
            name=xr_name + "-pab",
        ),
        spec=pabv1beta1.Spec(
            forProvider=pabv1beta1.ForProvider(
                region=params.region,
                bucketRef=pabv1beta1.BucketRef(
                    name = bucket_name,
                ),
                blockPublicAcls=False,
                ignorePublicAcls=False,
                restrictPublicBuckets=False,
                blockPublicPolicy=False,
            )
        )
    )
    resource.update(rsp.desired.resources[pab.metadata.name], pab)

    sse = ssev1beta1.BucketServerSideEncryptionConfiguration(
        apiVersion="s3.aws.upbound.io/v1beta1",
        kind="BucketServerSideEncryptionConfiguration",
        metadata=metav1.ObjectMeta(
            name=xr_name + "-encryption",
        ),
        spec=ssev1beta1.Spec(
            forProvider=ssev1beta1.ForProvider(
                region=params.region,
                bucketRef=ssev1beta1.BucketRef(
                    name=bucket_name,
                ),
                rule=[
                    ssev1beta1.RuleItem(
                        applyServerSideEncryptionByDefault=[
                            ssev1beta1.ApplyServerSideEncryptionByDefaultItem(
                                sseAlgorithm="AES256",
                            ),
                        ],
                        bucketKeyEnabled=True,
                    ),
                ],
            ),
        ),
    )
    resource.update(rsp.desired.resources[sse.metadata.name], sse)

    if params.versioning:
        versioning = verv1beta1.BucketVersioning(
            apiVersion="s3.aws.upbound.io/v1beta1",
            kind="BucketVersioning",
            metadata=metav1.ObjectMeta(
                name=xr_name + "-versioning",
            ),
            spec=verv1beta1.Spec(
                forProvider=verv1beta1.ForProvider(
                    region=params.region,
                    bucketRef=verv1beta1.BucketRef(
                        name=bucket_name,
                    ),
                    versioningConfiguration=[
                        verv1beta1.VersioningConfigurationItem(
                            status="Enabled",
                        ),
                    ],
                ),
            )
        )
        resource.update(rsp.desired.resources[versioning.metadata.name], versioning)
