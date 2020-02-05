import pytest
import sys
import os

from qgis.core import QgsApplication, QgsProcessingFeedback
from qgis.analysis import QgsNativeAlgorithms


def test_processing():

    qgis_root = r'/usr/share/qgis'
    QgsApplication.setPrefixPath(qgis_root, True)
    qgs = QgsApplication([], False)
    qgs.initQgis()

    # Add the path to processing so we can import it next
    processing_path = qgis_root + "/python/plugins"
    sys.path.insert(0, processing_path)

    # Imports usually should be at the top of a script but this unconventional
    # order is necessary here because QGIS has to be initialized first
    import processing
    from processing.core.Processing import Processing

    Processing.initialize()
    QgsApplication.processingRegistry().addProvider(QgsNativeAlgorithms())
    feedback = QgsProcessingFeedback()

    rivers = r'/home/david/workspace/comarques.shp'
    output = r'/home/david/workspace/result.shp'
    if not os.path.exists(rivers):
        print("File not found")

    expression = "NOM_COMAR LIKE '%Urgell%'"
    result = processing.run(
        'native:extractbyexpression',
        {'INPUT': rivers, 'EXPRESSION': expression, 'OUTPUT': output}, feedback=feedback
    )['OUTPUT']

