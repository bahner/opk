#!/usr/bin/env python3
# coding: utf-8
"""Constants for parsing list"""

COLUMNS = {
    "member_id": "A",
    "member_type": "B",
    "name": "C",
    "address_1": "D",
    "address_2": "E",
    "zip": "F",
    "postal": "G",
    "email": "H",
    "e_info": "I",
    "phone_private": "J",
    "phone_work": "K",
    "phone_mobile": "L",
    "fax": "M",
    "date_of_birth": "N",
    "start_date": "O",
    "balance": "P",
    "year_paid": "Q",
    "refund_period": "R",
    "last_updated": "S",
    "club_share": "T",
}

USED_COLUMNS = ((
    'member_id',
    'name',
    'email',
    'member_type',
))

MEMBER_TYPES = ((
    'BARN',
    'FAMILIE',
    'JUNIOR',
    'PENSJONIST',
    'SENIOR',
    'SPESIALMEDLEM',
    'STØTTEMEDLEM',
    'UNGDOM',
))
