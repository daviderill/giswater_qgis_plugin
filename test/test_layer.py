import pytest
import unittest
import sys
import os

from qgis.core import QgsApplication, QgsProviderRegistry, QgsVectorLayer
from qgis.analysis import QgsNativeAlgorithms


class TestPowerFunction(unittest.TestCase):

    def test_layer(self):

        """
        # default QGIS plugins
        export PYTHONPATH = "${PYTHONPATH}:/usr/local/share/qgis/python/plugins"
        # user installed plugins
        export PYTHONPATH = "${PYTHONPATH}:${HOME}/.qgis2/python/plugins"
        """

        qgis_root = r'/usr/share/qgis'
        plugins_path = qgis_root + "/python/plugins"
        QgsApplication.setPrefixPath(qgis_root, True)
        qgs = QgsApplication([], False)
        qgs.initQgis()

        # Add the path to processing so we can import it next
        processing_path = qgis_root + "/python/plugins"
        sys.path.insert(0, processing_path)

        aux = len(QgsProviderRegistry.instance().providerList())
        if aux == 0:
            raise RuntimeError('No data providers available.')

        # Check using assertion versus normal check
        layer_path = r'/home/david/workspace/comarques.shp'
        self.assertTrue(os.path.exists(layer_path), f"File not found: {layer_path}")
        if not os.path.exists(layer_path):
            print("File not found")
            return

        layer = QgsVectorLayer(layer_path, 'input', 'ogr')

        # Check using assertion versus normal check
        self.assertTrue(layer.isValid(), 'Failed to load "{}".'.format(layer.source()))
        if not layer.isValid():
            print("Layer failed to load: " + layer_path)

        self.assertEqual(layer.dataProvider().featureCount(), 41)

        # Add layer to TOC and canvas
        #QgsProject.instance().addMapLayer(vector_layer)

        # Zoom to layer
        #iface.mapCanvas().setExtent(vector_layer.extent())

