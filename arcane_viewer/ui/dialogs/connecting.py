"""
    Author: Jean-Pierre LESUEUR (@DarkCoderSc)
    License: Apache License 2.0
    More information about the LICENSE on the LICENSE file in the root directory of the project.
"""

from typing import Optional, Union

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (QDialog, QHBoxLayout, QLabel, QMainWindow,
                             QProgressBar, QSizePolicy, QSpacerItem,
                             QVBoxLayout)

import arcane_viewer.arcane as arcane
import arcane_viewer.ui.utilities as utilities


class ConnectingDialog(utilities.QCenteredDialog):
    def __init__(self, parent: Optional[Union[QDialog, QMainWindow]] = None) -> None:
        super().__init__(parent)

        self.setWindowTitle("📡 连接中...")

        window_flags = (Qt.WindowType.Dialog |
                        Qt.WindowType.FramelessWindowHint)

        self.setWindowFlags(window_flags)

        core_layout = QHBoxLayout()
        self.setLayout(core_layout)

        # Display Icon to the Left
        icon = QLabel(self)
        icon.setPixmap(QIcon(arcane.APP_ICON).pixmap(QSize(96, 96)))
        icon.setAlignment(Qt.AlignmentFlag.AlignCenter)
        core_layout.addWidget(icon)

        # Display Information to the Right
        info_layout = QVBoxLayout()
        core_layout.addLayout(info_layout)

        spacer_top = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        info_layout.addItem(spacer_top)

        label = QLabel("正在连接到远程服务器，请稍候...")
        info_layout.addWidget(label)

        progress_bar = QProgressBar()
        progress_bar.setRange(0, 0)
        info_layout.addWidget(progress_bar)

        spacer_bottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        info_layout.addItem(spacer_bottom)
