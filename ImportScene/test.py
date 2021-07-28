from FbxCommon import *
from DisplayMesh import *
from fbx import *


if __name__ == '__main__':

    lSdkManager, lScene = InitializeSdkObjects()

    lResult = LoadScene(lSdkManager, lScene, "ttt.fbx")

    rootNode = lScene.GetRootNode()

    if rootNode:
        for i in range(rootNode.GetChildCount()):
            childNode = rootNode.GetChild(i)
            lAttributeType = childNode.GetNodeAttribute().GetAttributeType()

            if lAttributeType == FbxNodeAttribute.eMesh:
                DisplayMesh(childNode)
