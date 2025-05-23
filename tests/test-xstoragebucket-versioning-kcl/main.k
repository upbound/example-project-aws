import models.com.example.platform.v1alpha1 as platformv1alpha1
import models.io.upbound.aws.s3.v1beta1 as s3v1beta1
import models.io.upbound.dev.meta.v1alpha1 as metav1alpha1

_items = [
    metav1alpha1.CompositionTest{
        metadata.name="test-xstoragebucket-versioning-kcl"
        spec= {
            assertResources: [
                platformv1alpha1.XStorageBucket{
                    metadata.name: "example-kcl"
                    spec.parameters: {
                        acl: "public-read"
                        region: "eu-central-1"
                        versioning: False
                    }
                }
                s3v1beta1.BucketACL{
                    metadata.name: "example-kcl-acl"
                    spec.forProvider:{
                        acl: "public-read"
                        bucketRef: {
                            name: "example-kcl-bucket"
                        }
                        region: "eu-central-1"
                    }
                }
                s3v1beta1.BucketOwnershipControls{
                    metadata.name: "example-kcl-boc"
                    spec.forProvider: {
                        bucketRef: {
                            name: "example-kcl-bucket"
                        }
                        region: "eu-central-1"
                        rule: [
                            {
                                objectOwnership: "BucketOwnerPreferred"
                            }
                        ]
                    }
                }
                s3v1beta1.Bucket{
                    metadata.name: "example-kcl-bucket"
                    spec.forProvider: {
                        region: "eu-central-1"
                    }
                }
                s3v1beta1.BucketServerSideEncryptionConfiguration{
                    metadata.name: "example-kcl-encryption"
                    spec.forProvider: {
                        bucketRef: {
                            name: "example-kcl-bucket"
                        }
                        region: "eu-central-1"
                        rule: [
                            {
                                applyServerSideEncryptionByDefault: [
                                    {
                                        sseAlgorithm: "AES256"
                                    }
                                ]
                                bucketKeyEnabled: True
                            }
                        ]
                    }
                }
                s3v1beta1.BucketPublicAccessBlock{
                    metadata.name: "example-kcl-pab"
                    spec.forProvider: {
                        blockPublicAcls: False
                        blockPublicPolicy: False
                        bucketRef: {
                            name: "example-kcl-bucket"
                        }
                        ignorePublicAcls: False
                        region: "eu-central-1"
                        restrictPublicBuckets: False
                    }
                }
            ]
            compositionPath: "apis/kcl/composition.yaml"
            xr: platformv1alpha1.XStorageBucket{
                metadata.name: "example-kcl"
                spec: {
                    compositionSelector: {
                        matchLabels: {
                            language="kcl"
                        }
                    }
                    parameters: {
                        versioning: False
                        acl: "public-read"
                        region: "eu-central-1"
                    }
                }
            }
            xrdPath: "apis/xstoragebuckets/definition.yaml"
            timeoutSeconds: 120
            validate: False
        }
    }
]
items = _items
