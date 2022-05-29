from email import message
from encodings import utf_8
import encodings
from glob import glob
from json.tool import main
import logging
import string
from telegram import KeyboardButton, ReplyKeyboardMarkup, Update, InlineKeyboardButton, InlineKeyboardMarkup
import os

from threading import TIMEOUT_MAX
import telegram
from telegram.ext import (
    CommandHandler,
    ContextTypes,
    Updater,
    MessageHandler,
    Filters,
    CallbackContext,
    CallbackQueryHandler,
)

sub_menu = ""
#######################################################################################################
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

#######################################################################################################


def start_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        "يا اهلاً ويا سهلاً ، هذا البوت صمم خصيصاً لمساعدة طلاب جامعة جازان 😎🌹")
    main_page(update, context)

#######################################################################################################


def main_page(update: Update, context: CallbackContext):
    keyboard = ReplyKeyboardMarkup([
        [KeyboardButton("البلاك بورد"), KeyboardButton(
            "القبول"), KeyboardButton("الطلبة")],
        [KeyboardButton("المكافأة"), KeyboardButton(
            "الخطط والقروبات الجامعية")], [KeyboardButton("الحركات الاكاديمية"), KeyboardButton("خدمة تواصل")]
    ], resize_keyboard=True, one_time_keyboard=False)
    update.message.reply_text(
        "اختار/ي القسم المناسب يا حلو/ة", reply_markup=keyboard)
#######################################################################################################


def student(update: Update, context: CallbackContext):
    global sub_menu
    sub_menu = "1"
    keyboard = ReplyKeyboardMarkup([
        [KeyboardButton("المنتظمون"), KeyboardButton(
            "المستجدون")],
        [KeyboardButton("الخريجون")], [KeyboardButton(
            "🔙 رجوع"), KeyboardButton("🔝 القائمة الرئيسية")]
    ], resize_keyboard=True, one_time_keyboard=False)
    update.message.reply_text("حدد نوع طلبك ؟", reply_markup=keyboard)

#######################################################################################################


def new_student(update: Update, context: CallbackContext):
    global sub_menu
    sub_menu = "2"
    keyboard = ReplyKeyboardMarkup([
        [KeyboardButton("طريقة الدخول الى موقع الجامعة")],
        [KeyboardButton("نظام الدراسة"), KeyboardButton("ألية احتساب المعدل")],
        [KeyboardButton("الايميل الجامعي"), KeyboardButton("تحديث الايبان")],
        [KeyboardButton("تسجيل المجموعات"),
         KeyboardButton("نموذج الكشف الطبي")],
        [KeyboardButton("ارفاق الصورة للبطاقة الجامعية")],
        [KeyboardButton(
            "🔙 رجوع"), KeyboardButton("🔝 القائمة الرئيسية")]
    ], resize_keyboard=True, one_time_keyboard=False)
    update.message.reply_text(
        "اختار/ي استفسارك بخصوص المستجدون ⬇️", reply_markup=keyboard)

#######################################################################################################


def attach_univ_photo(update: Update, context: CallbackContext):
    update.message.reply_text(
        '''⭕️ للطلبة المستجدين

    يمكنك طلب الحصول على البطاقة الجامعية من خلال الدخول لحسابك على النظام الأكاديمي وإدراج صورة شخصية مع ملاحظة الآتي :
    ‏- أن تكون الصورة حديثة وواضحة وملونة.
    - الالتزام بالزي (السعودي الرسمي)
    - صيغة الصورة (JPG)
    - استلام البطاقة الجامعية عن طريق الكلية بعد إعلان الكلية لذلك
    رابط النظام الأكاديمي: https://t.co/wTNivoDgYd‎''')

#######################################################################################################


def graudt_student(update: Update, context: CallbackContext):
    global sub_menu
    sub_menu = "2"
    keyboard = ReplyKeyboardMarkup([
        [KeyboardButton("استخراج السجل الاكاديمي")],
        [KeyboardButton("مراتب الشرف"), KeyboardButton(
            "تعديل وثيقة تخرج"), KeyboardButton("استلام الوثائق")],
        [KeyboardButton("تصديق طبق الأصل"), KeyboardButton(
            "تحديث الاسم")],
        [KeyboardButton(
            "🔙 رجوع"), KeyboardButton("🔝 القائمة الرئيسية")]
    ], resize_keyboard=True, one_time_keyboard=False)
    update.message.reply_text(
        "حدد نوع طلبك ؟", reply_markup=keyboard)
#######################################################################################################


def regular_student(update: Update, context: CallbackContext):
    global sub_menu
    sub_menu = "2"
    keyboard = ReplyKeyboardMarkup([
        [KeyboardButton("تاجيل الدراسة"), KeyboardButton(
            "الحذف والإضافة"), KeyboardButton("تسجيل المجموعات")],
        [KeyboardButton("الاعتذار عن مقرر"), KeyboardButton(
            "الانقطاع عن الدراسة"), KeyboardButton("اعادة القيد")],
        [KeyboardButton("الفصل من الجامعة"), KeyboardButton(
            "استخراج السجل الأكاديمي")],
        [KeyboardButton("اعتذار عن فصل دراسي"), KeyboardButton(
            "المواظبة و الحضور والغياب")],
        [KeyboardButton(
            "🔙 رجوع"), KeyboardButton("🔝 القائمة الرئيسية")]
    ], resize_keyboard=True, one_time_keyboard=False)
    update.message.reply_text(
        "اختار/ي استفسارك بخصوص المنتظمون ⬇️", reply_markup=keyboard)


#######################################################################################################

def enter_to_univ_website(update: Update, context: CallbackContext):
    '''
    طريقة الدخول الى موقع الجامعة
    '''
    context.bot.send_video(update.message.chat_id, 'https://www.learningcontainer.com/wp-content/uploads/2020/05/sample-mp4-file.mp4',
                           supports_streaming=True, caption="فيديو توضيحي لعملية ادخال بيانات القبول وترتيب الرغبات")

#######################################################################################################


def average_cal(update: Update, context: CallbackContext):
    '''
    ألية احتساب المعدل
    '''
    context.bot.send_photo(update.message.chat_id, 'https://i.postimg.cc/C5dBvTZQ/average-calculation.jpg',
                           caption="")

#######################################################################################################


def univ_email(update: Update, context: CallbackContext):
    '''
    الايميل الجامعي
    '''
    context.bot.send_document(update.message.chat_id, 'https://opennetworking.org/wp-content/uploads/2013/02/SDN-architecture-overview-1.0.pdf',
                              caption="")

#######################################################################################################


def echo(update: Update, context: ContextTypes):
    global sub_menu
    msg = update.message.text

    if(msg == "🔝 القائمة الرئيسية"):
        main_page(update, context)
    if(msg == "الطلبة"):
        student(update, context)
    if(msg == "المستجدون"):
        new_student(update, context)
    if(msg == "الخريجون"):
        graudt_student(update, context)
    if(msg == "المنتظمون"):
        regular_student(update, context)
    if (msg == "ارفاق الصورة للبطاقة الجامعية"):
        attach_univ_photo(update, context)
    if(msg == "ألية احتساب المعدل"):
        average_cal(update, context)
    if(msg == "طريقة الدخول الى موقع الجامعة"):
        enter_to_univ_website(update, context)
    if(msg == "الايميل الجامعي"):
        univ_email(update, context)
    if (msg == "🔙 رجوع" and sub_menu == "1"):
        main_page(update, context)
    if (msg == "🔙 رجوع" and sub_menu == "2"):
        student(update, context)


#######################################################################################################
if __name__ == '__main__':
    updater = Updater(token='5072934959:AAFQTzH2qkLh6tXPfcRAtyIKVmHQmnWeFI8', request_kwargs={
        'read_timeout': 1000, 'connect_timeout': 1000})
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start_handler))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    updater.start_polling()
    updater.idle()
