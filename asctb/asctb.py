# Auto generated from asctb.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-12-15T12:57:58
# Schema: asctb
#
# id: https://w3id.org/asctb
# description: asctb
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Integer, String, Uri
from linkml_runtime.utils.metamodelcore import URI

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BFO = CurieNamespace('BFO', 'http://purl.obolibrary.org/obo/BFO_')
CL = CurieNamespace('CL', 'http://purl.obolibrary.org/obo/CL_')
RO = CurieNamespace('RO', 'http://purl.obolibrary.org/obo/RO_')
UBERON = CurieNamespace('UBERON', 'http://purl.obolibrary.org/obo/UBERON_')
ASCTB = CurieNamespace('asctb', 'https://w3id.org/asctb')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = ASCTB


# Types
class CLIdentifier(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "CL identifier"
    type_model_uri = ASCTB.CLIdentifier


class HGNCIdentifier(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "HGNC identifier"
    type_model_uri = ASCTB.HGNCIdentifier


class Identifier(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "identifier"
    type_model_uri = ASCTB.Identifier


class UBERONIdentifier(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "UBERON identifier"
    type_model_uri = ASCTB.UBERONIdentifier


class FMAIdentifier(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "FMA identifier"
    type_model_uri = ASCTB.FMAIdentifier


class DOI(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "DOI"
    type_model_uri = ASCTB.DOI


class AnatomicalLabel(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "Anatomical label"
    type_model_uri = ASCTB.AnatomicalLabel


class CellTypeLabel(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "Cell type label"
    type_model_uri = ASCTB.CellTypeLabel


class CoordinateType(Integer):
    type_class_uri = XSD.integer
    type_class_curie = "xsd:integer"
    type_name = "CoordinateType"
    type_model_uri = ASCTB.CoordinateType


# Class references
class VesselClassVessel(AnatomicalLabel):
    pass


@dataclass
class VesselClass(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ASCTB.VesselClass
    class_class_curie: ClassVar[str] = "asctb:VesselClass"
    class_name: ClassVar[str] = "VesselClass"
    class_model_uri: ClassVar[URIRef] = ASCTB.VesselClass

    Vessel: Union[str, VesselClassVessel] = None
    BranchesFrom: Optional[Union[str, AnatomicalLabel]] = None
    VesselType: Optional[Union[str, "VesselTypeEnum"]] = None
    BodyPart: Optional[Union[str, AnatomicalLabel]] = None
    Sex: Optional[Union[str, "SexEnum"]] = None
    Anastomoses: Optional[Union[str, AnatomicalLabel]] = None
    ForBranchesSee: Optional[Union[str, AnatomicalLabel]] = None
    MergedVessel: Optional[Union[str, "IsVirtualMergedVessel"]] = None
    CoordX: Optional[Union[int, CoordinateType]] = None
    CoordY: Optional[Union[int, CoordinateType]] = None
    BranchSequence: Optional[int] = None
    CellType: Optional[Union[str, "CellTypeEnum"]] = None
    CellTypeLabel: Optional[Union[str, "CellTypeLabelEnum"]] = None
    CellTypeID: Optional[Union[str, CLIdentifier]] = None
    Biomarkers: Optional[str] = None
    BiomarkersLabel: Optional[str] = None
    BiomarkersID: Optional[Union[str, HGNCIdentifier]] = None
    ReferenceURL: Optional[Union[str, URI]] = None
    Reference: Optional[str] = None
    ReferenceDOI: Optional[Union[str, DOI]] = None
    UBERON: Optional[Union[str, UBERONIdentifier]] = None
    FMA: Optional[Union[str, FMAIdentifier]] = None
    BodyPartUberon: Optional[Union[str, UBERONIdentifier]] = None
    UBERONLabel: Optional[Union[str, AnatomicalLabel]] = None
    FMALabel: Optional[Union[str, AnatomicalLabel]] = None
    PathFromHeart: Optional[Union[str, AnatomicalLabel]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.Vessel):
            self.MissingRequiredField("Vessel")
        if not isinstance(self.Vessel, VesselClassVessel):
            self.Vessel = VesselClassVessel(self.Vessel)

        if self.BranchesFrom is not None and not isinstance(self.BranchesFrom, AnatomicalLabel):
            self.BranchesFrom = AnatomicalLabel(self.BranchesFrom)

        if self.VesselType is not None and not isinstance(self.VesselType, VesselTypeEnum):
            self.VesselType = VesselTypeEnum(self.VesselType)

        if self.BodyPart is not None and not isinstance(self.BodyPart, AnatomicalLabel):
            self.BodyPart = AnatomicalLabel(self.BodyPart)

        if self.Sex is not None and not isinstance(self.Sex, SexEnum):
            self.Sex = SexEnum(self.Sex)

        if self.Anastomoses is not None and not isinstance(self.Anastomoses, AnatomicalLabel):
            self.Anastomoses = AnatomicalLabel(self.Anastomoses)

        if self.ForBranchesSee is not None and not isinstance(self.ForBranchesSee, AnatomicalLabel):
            self.ForBranchesSee = AnatomicalLabel(self.ForBranchesSee)

        if self.MergedVessel is not None and not isinstance(self.MergedVessel, IsVirtualMergedVessel):
            self.MergedVessel = IsVirtualMergedVessel(self.MergedVessel)

        if self.CoordX is not None and not isinstance(self.CoordX, CoordinateType):
            self.CoordX = CoordinateType(self.CoordX)

        if self.CoordY is not None and not isinstance(self.CoordY, CoordinateType):
            self.CoordY = CoordinateType(self.CoordY)

        if self.BranchSequence is not None and not isinstance(self.BranchSequence, int):
            self.BranchSequence = int(self.BranchSequence)

        if self.CellType is not None and not isinstance(self.CellType, CellTypeEnum):
            self.CellType = CellTypeEnum(self.CellType)

        if self.CellTypeLabel is not None and not isinstance(self.CellTypeLabel, CellTypeLabelEnum):
            self.CellTypeLabel = CellTypeLabelEnum(self.CellTypeLabel)

        if self.CellTypeID is not None and not isinstance(self.CellTypeID, CLIdentifier):
            self.CellTypeID = CLIdentifier(self.CellTypeID)

        if self.Biomarkers is not None and not isinstance(self.Biomarkers, str):
            self.Biomarkers = str(self.Biomarkers)

        if self.BiomarkersLabel is not None and not isinstance(self.BiomarkersLabel, str):
            self.BiomarkersLabel = str(self.BiomarkersLabel)

        if self.BiomarkersID is not None and not isinstance(self.BiomarkersID, HGNCIdentifier):
            self.BiomarkersID = HGNCIdentifier(self.BiomarkersID)

        if self.ReferenceURL is not None and not isinstance(self.ReferenceURL, URI):
            self.ReferenceURL = URI(self.ReferenceURL)

        if self.Reference is not None and not isinstance(self.Reference, str):
            self.Reference = str(self.Reference)

        if self.ReferenceDOI is not None and not isinstance(self.ReferenceDOI, DOI):
            self.ReferenceDOI = DOI(self.ReferenceDOI)

        if self.UBERON is not None and not isinstance(self.UBERON, UBERONIdentifier):
            self.UBERON = UBERONIdentifier(self.UBERON)

        if self.FMA is not None and not isinstance(self.FMA, FMAIdentifier):
            self.FMA = FMAIdentifier(self.FMA)

        if self.BodyPartUberon is not None and not isinstance(self.BodyPartUberon, UBERONIdentifier):
            self.BodyPartUberon = UBERONIdentifier(self.BodyPartUberon)

        if self.UBERONLabel is not None and not isinstance(self.UBERONLabel, AnatomicalLabel):
            self.UBERONLabel = AnatomicalLabel(self.UBERONLabel)

        if self.FMALabel is not None and not isinstance(self.FMALabel, AnatomicalLabel):
            self.FMALabel = AnatomicalLabel(self.FMALabel)

        if self.PathFromHeart is not None and not isinstance(self.PathFromHeart, AnatomicalLabel):
            self.PathFromHeart = AnatomicalLabel(self.PathFromHeart)

        super().__post_init__(**kwargs)


# Enumerations
class CellTypeLabelEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="CellTypeLabelEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "blood vessel endothelial cell",
                PermissibleValue(text="blood vessel endothelial cell",
                                 description="blood vessel endothelial cell",
                                 meaning=CL["0000071"]) )
        setattr(cls, "cardiac endothelial cell",
                PermissibleValue(text="cardiac endothelial cell",
                                 description="cardiac endothelial cell",
                                 meaning=CL["0010008"]) )

class CellTypeEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="CellTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "blood vessel endothelial cell",
                PermissibleValue(text="blood vessel endothelial cell",
                                 description="blood vessel endothelial cell",
                                 meaning=CL["0000071"]) )
        setattr(cls, "cardiac endothelial cell",
                PermissibleValue(text="cardiac endothelial cell",
                                 description="cardiac endothelial cell",
                                 meaning=CL["0010008"]) )

class SexEnum(EnumDefinitionImpl):

    female = PermissibleValue(text="female",
                                   description="female organism",
                                   meaning=UBERON["0003100"])
    male = PermissibleValue(text="male",
                               description="male organism",
                               meaning=UBERON["0003101"])

    _defn = EnumDefinition(
        name="SexEnum",
    )

class VesselTypeEnum(EnumDefinitionImpl):

    arteriole = PermissibleValue(text="arteriole",
                                         description="arteriole",
                                         meaning=UBERON["0001980"])
    artery = PermissibleValue(text="artery",
                                   description="artery",
                                   meaning=UBERON["0001637"])
    capillary = PermissibleValue(text="capillary",
                                         description="capillary",
                                         meaning=UBERON["0001982"])
    sinus = PermissibleValue(text="sinus",
                                 description="sinus")
    sinusoid = PermissibleValue(text="sinusoid",
                                       description="sinusoid",
                                       meaning=UBERON["0003909"])
    vein = PermissibleValue(text="vein",
                               description="vein",
                               meaning=UBERON["0001638"])
    venule = PermissibleValue(text="venule",
                                   description="venule",
                                   meaning=UBERON["0001979"])

    _defn = EnumDefinition(
        name="VesselTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "heart chamber",
                PermissibleValue(text="heart chamber",
                                 description="heart",
                                 meaning=UBERON["0000948"]) )

class IsVirtualMergedVessel(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="IsVirtualMergedVessel",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "0",
                PermissibleValue(text="0",
                                 description="is NOT virtual merged vessel used to show the branches of other vessels.") )
        setattr(cls, "1",
                PermissibleValue(text="1",
                                 description="is virtual merged vessel used to show the branches of other vessels.") )

# Slots
class slots:
    pass

slots.BranchesFrom = Slot(uri=ASCTB.BranchesFrom, name="BranchesFrom", curie=ASCTB.curie('BranchesFrom'),
                   model_uri=ASCTB.BranchesFrom, domain=None, range=Optional[Union[str, AnatomicalLabel]])

slots.Vessel = Slot(uri=SCHEMA.identifier, name="Vessel", curie=SCHEMA.curie('identifier'),
                   model_uri=ASCTB.Vessel, domain=None, range=URIRef)

slots.VesselType = Slot(uri=RDFS.subClassOf, name="VesselType", curie=RDFS.curie('subClassOf'),
                   model_uri=ASCTB.VesselType, domain=None, range=Optional[Union[str, "VesselTypeEnum"]])

slots.BodyPart = Slot(uri=BFO['0000050'], name="BodyPart", curie=BFO.curie('0000050'),
                   model_uri=ASCTB.BodyPart, domain=None, range=Optional[Union[str, AnatomicalLabel]])

slots.Sex = Slot(uri=SCHEMA.gender, name="Sex", curie=SCHEMA.curie('gender'),
                   model_uri=ASCTB.Sex, domain=None, range=Optional[Union[str, "SexEnum"]])

slots.Anastomoses = Slot(uri=RO['0002378'], name="Anastomoses", curie=RO.curie('0002378'),
                   model_uri=ASCTB.Anastomoses, domain=None, range=Optional[Union[str, AnatomicalLabel]])

slots.ForBranchesSee = Slot(uri=ASCTB.ForBranchesSee, name="ForBranchesSee", curie=ASCTB.curie('ForBranchesSee'),
                   model_uri=ASCTB.ForBranchesSee, domain=None, range=Optional[Union[str, AnatomicalLabel]])

slots.MergedVessel = Slot(uri=ASCTB.MergedVessel, name="MergedVessel", curie=ASCTB.curie('MergedVessel'),
                   model_uri=ASCTB.MergedVessel, domain=None, range=Optional[Union[str, "IsVirtualMergedVessel"]])

slots.CoordX = Slot(uri=ASCTB.CoordX, name="CoordX", curie=ASCTB.curie('CoordX'),
                   model_uri=ASCTB.CoordX, domain=None, range=Optional[Union[int, CoordinateType]])

slots.CoordY = Slot(uri=ASCTB.CoordY, name="CoordY", curie=ASCTB.curie('CoordY'),
                   model_uri=ASCTB.CoordY, domain=None, range=Optional[Union[int, CoordinateType]])

slots.BranchSequence = Slot(uri=ASCTB.BranchSequence, name="BranchSequence", curie=ASCTB.curie('BranchSequence'),
                   model_uri=ASCTB.BranchSequence, domain=None, range=Optional[int])

slots.CellType = Slot(uri=ASCTB.CellType, name="CellType", curie=ASCTB.curie('CellType'),
                   model_uri=ASCTB.CellType, domain=None, range=Optional[Union[str, "CellTypeEnum"]])

slots.CellTypeLabel = Slot(uri=ASCTB.CellTypeLabel, name="CellTypeLabel", curie=ASCTB.curie('CellTypeLabel'),
                   model_uri=ASCTB.CellTypeLabel, domain=None, range=Optional[Union[str, "CellTypeLabelEnum"]])

slots.CellTypeID = Slot(uri=ASCTB.CellTypeID, name="CellTypeID", curie=ASCTB.curie('CellTypeID'),
                   model_uri=ASCTB.CellTypeID, domain=None, range=Optional[Union[str, CLIdentifier]])

slots.Biomarkers = Slot(uri=ASCTB.Biomarkers, name="Biomarkers", curie=ASCTB.curie('Biomarkers'),
                   model_uri=ASCTB.Biomarkers, domain=None, range=Optional[str])

slots.BiomarkersLabel = Slot(uri=ASCTB.BiomarkersLabel, name="BiomarkersLabel", curie=ASCTB.curie('BiomarkersLabel'),
                   model_uri=ASCTB.BiomarkersLabel, domain=None, range=Optional[str])

slots.BiomarkersID = Slot(uri=ASCTB.BiomarkersID, name="BiomarkersID", curie=ASCTB.curie('BiomarkersID'),
                   model_uri=ASCTB.BiomarkersID, domain=None, range=Optional[Union[str, HGNCIdentifier]])

slots.ReferenceURL = Slot(uri=ASCTB.ReferenceURL, name="ReferenceURL", curie=ASCTB.curie('ReferenceURL'),
                   model_uri=ASCTB.ReferenceURL, domain=None, range=Optional[Union[str, URI]])

slots.Reference = Slot(uri=ASCTB.Reference, name="Reference", curie=ASCTB.curie('Reference'),
                   model_uri=ASCTB.Reference, domain=None, range=Optional[str])

slots.ReferenceDOI = Slot(uri=ASCTB.ReferenceDOI, name="ReferenceDOI", curie=ASCTB.curie('ReferenceDOI'),
                   model_uri=ASCTB.ReferenceDOI, domain=None, range=Optional[Union[str, DOI]])

slots.UBERON = Slot(uri=ASCTB.UBERON, name="UBERON", curie=ASCTB.curie('UBERON'),
                   model_uri=ASCTB.UBERON, domain=None, range=Optional[Union[str, UBERONIdentifier]])

slots.FMA = Slot(uri=ASCTB.FMA, name="FMA", curie=ASCTB.curie('FMA'),
                   model_uri=ASCTB.FMA, domain=None, range=Optional[Union[str, FMAIdentifier]])

slots.BodyPartUberon = Slot(uri=ASCTB.BodyPartUberon, name="BodyPartUberon", curie=ASCTB.curie('BodyPartUberon'),
                   model_uri=ASCTB.BodyPartUberon, domain=None, range=Optional[Union[str, UBERONIdentifier]])

slots.UBERONLabel = Slot(uri=ASCTB.UBERONLabel, name="UBERONLabel", curie=ASCTB.curie('UBERONLabel'),
                   model_uri=ASCTB.UBERONLabel, domain=None, range=Optional[Union[str, AnatomicalLabel]])

slots.FMALabel = Slot(uri=ASCTB.FMALabel, name="FMALabel", curie=ASCTB.curie('FMALabel'),
                   model_uri=ASCTB.FMALabel, domain=None, range=Optional[Union[str, AnatomicalLabel]])

slots.PathFromHeart = Slot(uri=ASCTB.PathFromHeart, name="PathFromHeart", curie=ASCTB.curie('PathFromHeart'),
                   model_uri=ASCTB.PathFromHeart, domain=None, range=Optional[Union[str, AnatomicalLabel]])