# -*- coding: utf-8 -*-
import base64

from odoo import SUPERUSER_ID
from odoo import http, _
from odoo.tools.translate import _
from odoo.http import request

from odoo.addons.website.models.website import slug

import logging
_logger = logging.getLogger(__name__)


class dpo_assistant(http.Controller):
    #@http.route('/services', type='http', auth="public", website=True)
    #def principal(self):
        #env = request.env(context=dict(request.env.context, show_address=True, no_tag_br=True))
        # Render page
    #    return request.render("dpo_assistant.thankyou", {})

    #@http.route('/aboutus', type='http', auth="public", website=True)
    #def aboutus(self):
        #env = request.env(context=dict(request.env.context, show_address=True, no_tag_br=True))
        # Render page
    #    return request.render("dpo_assistant.thankyou", {})


    #Ignore Mo Muna sir Unless I override mo yung Homepage
    #Overriding Homepage
    #@http.route('/page/homepage', type='http', auth="public", website=True)
    #def homepage(self):
        #env = request.env(context=dict(request.env.context, show_address=True, no_tag_br=True))
        # Render page
    #    return request.render("dpo_assistant.thankyou", {})


    @http.route('/page/contactus', type='http', auth="public", website=True)
    def contactus(self):
        #env = request.env(context=dict(request.env.context, show_address=True, no_tag_br=True))
        # Render page
        return request.render("dpo_assistant.contactus", {})



    @http.route('/page/inquire', type='http', auth="public", website=True)
    def submitdata(self, **kw):
        #Super ID which is ADMIN 1
        if not request.uid:
            request.uid = 1        

        #How to Call a Model in a Controller
        model_inquiries = http.request.env['dpo_assistant.inquiries'].sudo()


        result = model_inquiries.create({
            'name' : request.params['name'],
            'email': request.params['email'],
            'company': request.params['company'],
            'contact_number': request.params['contact_number'],
            'inq_type': request.params['type'],
            'message': request.params['message']
        })




        return request.render("dpo_assistant.thankyou", {})        


    #Ignore Mo Muna sir Unless I override mo yung Homepage
    #Overriding Homepage
    #@http.route('/page/homepage', type='http', auth="public", website=True)
    #def homepage(self):
        #env = request.env(context=dict(request.env.context, show_address=True, no_tag_br=True))
        # Render page
    #    return request.render("psvalliance.homepage", {})



    #@http.route('/page/subscribe', type='http', auth="public", website=True)
    #def submitdata(self, **kw):
        #Super ID which is ADMIN 1
    #    if not request.uid:
    #        request.uid = 1        

        #How to Call a Model in a Controller
     #   model_dpo_assistant_subscribers = http.request.env['dpo_assistant.subscribers'].sudo()


        #_logger.info('Name: ' + request.params['partner_name'])
        #_logger.info('Email: ' + request.params['partner_email'])
        #_logger.info('Company: ' + request.params['partner_company'])
        ##_logger.info('Contact Number: ' + request.params['partner_contactnumber'])
        #_logger.info('Message: ' + request.params['partner_message'])

        #Creation of New Record
    #    result = model_dpo_assistant_subscribers.create({
    #        'name' : request.params['name'],
    #        'email': request.params['email'],
    #        'company': request.params['company'],
    #        'contact_number': request.params['name'],
    #        'message': request.params['message']
    #    })




     #   return request.render("dpo_assistant.thankyou", {})        


    #Ignore Mo Muna sir Unless I override mo yung Homepage
    #Overriding Homepage
    #@http.route('/page/homepage', type='http', auth="public", website=True)
    #def homepage(self):
        #env = request.env(context=dict(request.env.context, show_address=True, no_tag_br=True))
        # Render page
    #    return request.render("dpo_assistant.homepage", {})

# vim :et:
