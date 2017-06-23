# -*- coding: utf-8 -*-
#
# django-codenerix-pos
#
# Copyright 2017 Centrologic Computational Logistic Center S.L.
#
# Project URL : http://www.codenerix.com
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.utils.translation import ugettext as _

from codenerix.views import GenList, GenCreate, GenCreateModal, GenUpdate, GenUpdateModal, GenDelete, GenDetail, GenDetailModal

from .models import POS, POSSlot
from .forms import POSForm, POSSlotForm

# POS
class POSList(GenList):
    model = POS
    show_details = True
    extra_context = {
        'menu': ['pos', 'pos'],
        'bread': [_('POS'), _('POS')]
    }


class POSCreate(GenCreate):
    model = POS
    form_class = POSForm


class POSCreateModal(GenCreateModal, POSCreate):
    pass


class POSUpdate(GenUpdate):
    model = POS
    form_class = POSForm


class POSUpdateModal(GenUpdateModal, POSUpdate):
    pass


class POSDelete(GenDelete):
    model = POS


class POSDetails(GenDetail):
    model = POS

class POSDetailsModal(GenDetailModal, POSDetails):
    pass


# POSSlotSlot
class POSSlotList(GenList):
    model = POSSlot
    show_details = True
    extra_context = {
        'menu': ['pos', 'posslot'],
        'bread': [_('POS'), _('POSSlot')]
    }


class POSSlotCreate(GenCreate):
    model = POSSlot
    form_class = POSSlotForm


class POSSlotCreateModal(GenCreateModal, POSSlotCreate):
    pass


class POSSlotUpdate(GenUpdate):
    model = POSSlot
    form_class = POSSlotForm


class POSSlotUpdateModal(GenUpdateModal, POSSlotUpdate):
    pass


class POSSlotDelete(GenDelete):
    model = POSSlot


class POSSlotDetails(GenDetail):
    model = POSSlot

class POSSlotDetailsModal(GenDetailModal, POSSlotDetails):
    pass