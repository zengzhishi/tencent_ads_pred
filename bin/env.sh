#PATH ENV
WORK_PATH=`dirname $PWD`
BIN_PATH=$WORK_PATH/bin
CONF_PATH=$WORK_PATH/conf
LIB_PATH=$WORK_PATH/lib
DATA_PATH=$WORK_PATH/data
LOG_PATH=$WORK_PATH/log
OUTPUT_PATH=$WORK_PATH/output
TMP_PATH=$WORK_PATH/tmp
BAKUP_PATH=$WORK_PATH/bakup

LOG_WF_FILE=${LOG_PATH}/log.wf
LOG_FILE=${LOG_PATH}/log.n


function Write_Log_Fatal ()
{
    local time_day=`date +%m-%d`
    local time_hms=`date +%T`
    echo "FATAL: $time_day $time_hms $@" >> $LOG_WF_FILE;
    return 0
}

function Write_Log_Warning ()
{
    local time_day=`date +%m-%d`
    local time_hms=`date +%T`
    echo "WARNING: $time_day $time_hms $@" >> $LOG_WF_FILE;
    return 0
}

function Write_Log_Notice ()
{
    local time_day=`date +%m-%d`
    local time_hms=`date +%T`
    echo "NOTICE: $time_day $time_hms $@" >> $LOG_FILE;
    return 0
}
